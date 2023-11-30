# -- coding: utf-8 --
# date：2023/11/29 15:23
# author: ZhangXu

import time


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