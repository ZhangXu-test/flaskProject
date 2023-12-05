# -- coding: utf-8 --
# date：2023/11/29 15:23
# author: ZhangXu

import time
import functools


"""
def time_decorator(function):
    def wrapper():
        start_time = time.time()
        function()
        end_time = time.time()
        print(f"函数执行时间：{end_time - start_time:.3f} 秒")
    return wrapper


@time_decorator
def my_function():
    # 函数的实现
    for i in range(10000):
        print(i)


if __name__ == '__main__':
    my_function()
"""


def auth1(func):
    print("1")

    @functools.wraps(func)
    def inner(*args, **kwargs):
        return func(*args, **kwargs)
    return inner


def auth2(func):
    print("2")

    @functools.wraps(func)
    def inner(*args, **kwargs):
        return func(*args, **kwargs)
    return inner


@auth1
@auth2
def index():
    pass



