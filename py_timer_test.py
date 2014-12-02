# Copyright 2014 Sean Donovan
# Tests for py_timer


from py_timer import py_timer as Timer
import threading
import time

def basic_test():
    def basic_test_print_1():
        print "Basic Test 1"
        print "Threads: " + str(threading.active_count())

    def basic_test_print_2():
        print "Basic Test 2"
        print "Threads: " + str(threading.active_count())

    def basic_test_print_3():
        print "Basic Test 3"
        print "Number of active threads: " + str(threading.active_count())

    print "basic_test begin"
    print "BEGIN: Number of active threads: " + str(threading.active_count())

    Timer(1, basic_test_print_1)
    Timer(2, basic_test_print_2)
    Timer(3, basic_test_print_3)

    time.sleep(5)
    print "END: Number of active threads: " + str(threading.active_count())
    print "basic_test end"
    print ""
    print ""
    print ""


def basic_test_with_args():
    def basic_test_with_args_print(num):
        print "Basic Test with Args " + str(num)
        print "Threads: " + str(threading.active_count())

    print "basic_test_with_args begin"
    print "BEGIN: Number of active threads: " + str(threading.active_count())

    Timer(1, basic_test_with_args_print, [1])
    Timer(2, basic_test_with_args_print, [2])
    Timer(3, basic_test_with_args_print, [3])

    time.sleep(5)
    print "END: Number of active threads: " + str(threading.active_count())
    print "basic_test_with_args end"
    print ""
    print ""
    print ""

def basic_test_with_kwargs():
    def basic_test_with_kwargs_print(num=0):
        print "Basic Test with KWArgs " + str(num)
        print "Threads: " + str(threading.active_count())

    print "basic_test_with_kwargs begin"
    print "BEGIN: Number of active threads: " + str(threading.active_count())

    Timer(1, basic_test_with_kwargs_print, kwargs={'num':1})
    Timer(2, basic_test_with_kwargs_print, kwargs={'num':2})
    Timer(3, basic_test_with_kwargs_print, kwargs={'num':3})

    time.sleep(5)
    print "END: Number of active threads: " + str(threading.active_count())
    print "basic_test_with_kwargs end"
    print ""
    print ""
    print ""

def basic_test_with_args_and_kwargs():
    def basic_test_with_args_and_kwargs_print(num, num2=0):
        print "Basic Test with KWArgs " + str(num) + "  " + str(num2)
        print "Threads: " + str(threading.active_count())

    print "basic_test_with_args_and_kwargs begin"
    print "BEGIN: Number of active threads: " + str(threading.active_count())

    Timer(1, basic_test_with_args_and_kwargs_print, [1])
    Timer(2, basic_test_with_args_and_kwargs_print, kwargs={'num':2})
    Timer(3, basic_test_with_args_and_kwargs_print, kwargs={'num':3, 'num2':3})
    Timer(4, basic_test_with_args_and_kwargs_print, [4,4])
    Timer(5, basic_test_with_args_and_kwargs_print, [5], {'num2':5})

    time.sleep(7)
    print "END: Number of active threads: " + str(threading.active_count())
    print "basic_test_with_args_and_kwargs end"
    print ""
    print ""
    print ""

def insertion_to_tail():
    # This is what's happening everywhere. Not gonna implement this.
    pass

def insertion_to_middle():
    def test_print(num):
        print "Timer number " + str(num)
        print "Threads: " + str(threading.active_count())

    print "insertion_to_middle begin"
    print "BEGIN: Number of active threads: " + str(threading.active_count())

    Timer(1, test_print, [1])
    Timer(3, test_print, [3])
    Timer(2, test_print, [2])

    time.sleep(5)
    print "END: Number of active threads: " + str(threading.active_count())
    print "insertion_to_middle end"
    print ""
    print ""
    print ""


def insertion_to_head():
    def test_print(num):
        print "Timer number " + str(num)
        print "Threads: " + str(threading.active_count())

    print "insertion_to_head begin"
    print "BEGIN: Number of active threads: " + str(threading.active_count())

    Timer(2, test_print, [2])
    Timer(1, test_print, [1])
    Timer(3, test_print, [3])

    time.sleep(5)
    print "END: Number of active threads: " + str(threading.active_count())
    print "insertion_to_head end"
    print ""
    print ""
    print ""

def removal_from_tail():
    def test_print(num):
        print "Timer number " + str(num)
        print "Threads: " + str(threading.active_count())

    print "removal_from_tail begin"
    print "BEGIN: Number of active threads: " + str(threading.active_count())

    timer1 = Timer(1, test_print, [1])
    timer2 = Timer(2, test_print, [2])
    timer3 = Timer(3, test_print, [3])

    timer3.cancel()

    time.sleep(5)
    print "END: Number of active threads: " + str(threading.active_count())
    print "removal_from_tail end"
    print ""
    print ""
    print ""


def removal_from_middle():
    def test_print(num):
        print "Timer number " + str(num)
        print "Threads: " + str(threading.active_count())

    print "removal_from_tail begin"
    print "BEGIN: Number of active threads: " + str(threading.active_count())

    timer1 = Timer(1, test_print, [1])
    timer2 = Timer(2, test_print, [2])
    timer3 = Timer(3, test_print, [3])

    timer2.cancel()

    time.sleep(5)
    print "END: Number of active threads: " + str(threading.active_count())
    print "removal_from_tail end"
    print ""
    print ""
    print ""

def removal_from_head():
    def test_print(num):
        print "Timer number " + str(num)
        print "Threads: " + str(threading.active_count())

    print "removal_from_tail begin"
    print "BEGIN: Number of active threads: " + str(threading.active_count())

    timer1 = Timer(1, test_print, [1])
    timer2 = Timer(2, test_print, [2])
    timer3 = Timer(3, test_print, [3])

    timer1.cancel()

    time.sleep(5)
    print "END: Number of active threads: " + str(threading.active_count())
    print "removal_from_tail end"
    print ""
    print ""
    print ""

def timer_death_on_interrupt():
    # Create a long live timer, and have program end abruptly by having user
    # hit CTRL-C

    def test_print(num):
        print "Timer number " + str(num)
        print "Threads: " + str(threading.active_count())

    print "timer_death_on_interrupt begin"
    print "BEGIN: Number of active threads: " + str(threading.active_count())

    Timer(3600, test_print, [1])
    
    print "USER MUST HIT CTRL-C TO TEST"
    print "IF PROGRAM DIES BACK TO PROMPT, SUCCESSFUL TEST."
    print "IF PROGRAM HANGS FOR AN HOUR, UNSUCCESSFUL."
    time.sleep(3600)
    
    
if __name__ == '__main__':
    basic_test()
    basic_test_with_args()
    basic_test_with_kwargs()
    basic_test_with_args_and_kwargs()
    insertion_to_middle()
    insertion_to_head()
    removal_from_tail()
    removal_from_middle()
    removal_from_head()
    timer_death_on_interrupt()
