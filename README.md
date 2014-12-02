py-timer
========

List-based timers for Python to make it easier to actually use and kill timers. One thread overhead when a timer is active, rather than dozens of threads. 

This is based on an old technique for limiting the number of active timers outstanding to one. I wrote this because I was having lots of issues getting timers to die when the program died. Rather than try fighting with it, I wrote this wrapper.

# Usage
Use it as you would use Python's [built-in timers](https://docs.python.org/2/library/threading.html#timer-objects). 

You should be able to replace the current timers with the following import line:

    from py_timer import py_timer as Timer

Usage is the same as the built-in Timer:

    def hello_world():
        print "Hello World!"
    py_timer(5, hello_world)

This will print "Hello World!" after 5 seconds.

The timers can also accept arguments:

    def print_a_number(num):
        print "num = " + str(num)
    py_timer(5, print_a_number, [100])

And kwargs:

    py_timer(5, print_a_number, kwargs={'num':100})

Or both:

    def print_two_numbers(num, num2=0):
        print "num = " + str(num)
    py_timer(5, print_a_number, [100], {'num2': 100})

# Cancelling timers
Timers can be cancelled as with the built-in library:

    timer1 = py_timer(5, print_a_number, [100])
    timer1.cancel()

When the main program finishes, all timers will be canceled. Keep this in mind! It is implemented using [daemon](https://docs.python.org/2/library/threading.html#threading.Thread.daemon) threads (see the ``_restart_timer()`` function in ``py_timer_manager`` class).

# Limitations
Second resolution at this time. Only accepts in seconds, have not tested with partial seconds yet.
