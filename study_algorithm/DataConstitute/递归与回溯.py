#使用回溯求一个序列的所有可能排列
import threading,math,time
import matplotlib.pyplot as plt     #作图模块


def function():
    def bitStr(n,s):
        if n == 1:
            return s
        return [digit + bits for digit in bitStr(1, s) for bits in bitStr(n-1, s)]
    print(bitStr(3,'abc'))


bit = threading.Thread(target=function,daemon=True).start()

# x = list(range(1,100))
# l = []; l2 = []; l3 = []
# plt.plot(x,[y*y for y in x])    #作Y = x * x 的图像
# plt.plot(x, [(7*y)*math.log(y,2) for y in x])   #作y = 7xlog2(x)的图像
# plt.plot(x,[(6*y)*math.log(y,2) for y in x])
# plt.show()


#timeit函数：
"""
出现错误，问题未发现
        import timeit
        def test2(n):
            ls = []
            for i in range(n):
                t = timeit.timeit("nest(" + str(n) + ")", setup="from _main_ import nest", number=1)
                ls.append(t)
            return ls
        
        n = 1000
        plt.plot(test2(n))
        plt.plot([x*x/10000000 for x in range(n)])
"""

"""
    树状图的绘制
"""
import numpy as np
data = [[54,67,84,8,345,8],[23,42,64,14,54,67]]
x_value = np.arange(len(data[0]))
plt.bar(x_value + 0.00,data[0], width=0.2,color='grey')
plt.bar(x_value + 0.30,data[1], width=0.3,color='pink')
plt.show()

