# Decorators 

"""
A decorator is a function that wraps another function to extend 
or modify its behavior — without changing the original function's code.
"""

"""
Basic structure of a decorator:

def decorator_function(original_function):

    def wrapper():
        print("Before function runs")
        original_function()
        print("After function runs")

    return wrapper
"""

import time

def tick_tock(func):
    def wrapper(*args, **kwargs):
        t1 = time.time()
        func(*args, **kwargs)
        t2 = time.time() - t1
        print(f"Execution time: {t2:.4f} seconds")
    return wrapper

@tick_tock
def count_to_n(n):
    total = 0
    for i in range(1, n + 1):
        total += i
    print(f"Sum of numbers from 1 to {n} is {total}")

count_to_n(1000000)
