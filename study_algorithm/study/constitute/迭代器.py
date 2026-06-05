"""
    重写__iter__和__next__魔术方法可以创建一个迭代器
"""
from traceback import print_tb
import sys,math


class My_iteration:
    def __init__(self,start,end):
        self.start = start
        self.end = end

    def __iter__(self):
        return self

    def __next__(self):
        if self.end <= self.start:
            raise StopIteration
        else:
            self.start += 1
            return self.start - 1

for i in My_iteration(1,10):
    print(i)


# 生成器


print("-" * 32)

my = [i for i in My_iteration(1,1000000)]    # 这是一个列表

my_generator = (i for i in My_iteration(1,10000000))        #小括号的是一个生成器
print(f"这是一个list的内存空间大小：{sys.getsizeof(my)}")

#使用生成器可以节省内存空间，只有当程序员需要使用的时候才生成。

print(f"这是generator的内存空间：{sys.getsizeof(my_generator)}")
print(next(my_generator))
print(next(my_generator))
print('*' * 32)
# for i in my_generator:
#     print(i)


print('-' * 32)
"""
    使用yield函数来创建生成器:
    
"""
def my_gt(n):
    n = math.ceil(n)        #向上取整列如：2.6 = 3 ， 2.1 = 3
    for i in range(n):
        yield i

m = my_gt(10)
print(next(m))
print(next(m))
for i in m:
    print(i)