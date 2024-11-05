# def func_decorator(func):
#     def wrapper():
#         print("before")
#         func()
#         print("after")

#     return wrapper

# @func_decorator
# def some_func():
#     print("this is python")


# some_func()

import time


def func_decorator(func):
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        func()
        end = time.perf_counter()
        result = end - start
        print(result)

    return wrapper


@func_decorator
def some_func():
    print("hello")


some_func()
