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
