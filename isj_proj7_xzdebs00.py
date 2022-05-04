#!/usr/bin/env python3

import collections

my_counter = collections.Counter()

def log_and_count(key = None, counts = None):
    def log_and_count_decorator(func):
        def inner(*args, **kwargs):
            print(f"called {func.__name__} with {args} and {kwargs}")
            if counts is not None:
                counts.update({key if key is not None else func.__name__ : 1})
        return inner
        
    return log_and_count_decorator





@log_and_count(key = 'basic functions', counts = my_counter)
def f1(a, b=2):
    return a ** b

@log_and_count(key = 'basic functions', counts = my_counter)
def f2(a, b=3):
    return a ** 2 + b

@log_and_count(counts = my_counter)
def f3(a, b=5):
    return a ** 3 - b

f1(2)
f2(2, b=4)
f1(a=2, b=4)
f2(4)
f2(5)
f3(5)
f3(5,4)

print(my_counter)
