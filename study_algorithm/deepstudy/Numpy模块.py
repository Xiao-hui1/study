import numpy as np

#生成numpy.array数组

num = np.array([1,2,3,4,5])

print(type(num))

x = np.array([1,2,3,4,5])
y = np.array([1,2,3,4,5])
print(x+y)                  #长度相同可以直接进行运算，运算时是对应位置的值进行运算    不同长度是会报错
#将数组与一个常数进行运算是这个常数会对数组的每一位都进行计算
x = x * 2
#-------------------------------------------------------------------------
#arange 函数
warray = np.arange(10,2)  #生成一个数组，值是从 0-9 之间的所有偶数。
print(warray)

#linspace 函数
#通过指定起始值，终值和元素个数创建一维数组；
warray = np.linspace(1,2,5)

#logspace 函数  和linspace 类似，只是他创建的是等比数列，且基数为10，所有开始值和结束值是代表的（从10的几次幂到第几次幂）
warray = np.logspace(1,2,5)

#zeros ones 函数   创建指定长度和形状全为 0/1 的数组
warray = np.zeros([3,3])
warray = np.ones([3,3])

#diag eye 函数    创建对角线位置全为（指定数或0）(1)的矩阵
warray = np.diag([1,2,3])
warray = np.eye(3)


#---------------------------------------------------------------------------------
"""
    ndim    秩，即数据轴的个数
    shape   数组的维数
    size    数组的元素个数
    dtype   数据类型
    itemsize    数组中每个元素的字节大小
"""
#np.array可以生成多维数组，使用  数组名.shape可以得到数组的形状，使用 数组名.dtype可以得到数组的数据类型
print(x.shape)
print(x.dtype)
num = np.arange(10)
num.shape = 2,5 #改变数组现在的形状
num2 = num.reshape(2,-1) #效果同上，这里-1表示根据自身来改变宽度。
num1 = num.astype(np.float32)   #改变数据类型


"""
    random  生成随机数
        randint 随机整数
        rand    生成[0,1]的随机数
"""


"""
    hstack  和 vstack 和 concatenate 函数   横向合并 和 纵向合并
    hsplit  vsplit split 横向分割...
"""

print('-'*64)
arr1 = np.arange(20).reshape(5,4)
arr2 = arr1*2
arr3 = np.hstack((arr1,arr2))   #使用横向合并
arr4 = np.concatenate((arr1,arr2),axis=1) #等价于上面 axis = 0 则为纵向合并
print(arr3)
print(np.hsplit(arr3,4))    #把原数组分割成多个数组，但是分割数要能被数组的一维长度整除，否则会报错误.
print(np.split(arr3,[2,3]))  #在第二行 和 第三行处分割。】

print('-'*64)

""" transpose   转置函数"""
arr = np.arange(6).reshape(3,2)
print(arr.swapaxes(0,1))    #效果同下
print(arr.transpose(1,0))   #需要传入轴编号组成的元组  也可以使用数组的T属性来进行转置。
print('-'*64)


""" ufunc 函数    这个并非一个真正的函数，而是指一指方式。"""
#在数组运算时维数可以不同，但是一维的长度必须相同。
x = np.array([[1,2,3,4,5],[2,3,4,5,6]])
x = x * y
print(x)    #input :[[ 1  4  9 16 25],[ 2  6 12 20 30]]

""" where(condition,x,y)    condition = True 输出 x 否则 y """
print(np.where([[True,False],[True,False]],[[12,23],[34,45]],[[56,67],[78,89]]))

i  =  10/2      #注意在python中 int / int = float
print(f"i = {i: .0f}")  #不带小数的输出
print(type(i))  #float

"""     
    数组的读写
        Numpy.load("文件名.npy") 读
        Numpy.save("文件名.npy",arr)   写
        Numpy.savez("文件名.npy",arr,s,x)  多数组的保存
    文本文件的读写：
        Numpy.loadtxt("file.txt",delimiter = ",")   把文件加载到二维数组中
        Numpy.savetxt("file.txt", arr,fmt = "%d", delimiter = ",")  将数组中写到某种分隔符隔开的文本文件中 delimiter 是指定的分隔符
        Numpy.genfromtxt("file.txt", delimiter = ",")   结构化数组和缺失的数据
    CSV文件读取：
        loadtxt(fname,dtype=,comments = '#',delimiter = None,converters =None,skiprows = 0,usecols = None,unpack = False,
        ndimin = 0,encodeing = 'bytes')
        
        fname   str,读取的CSV文件名
        delimiter   str,数据的分隔符
        usecols     tuple(元组)，执行加载数组文件中有那些列
        unpack      bool,是否将加载的数据拆分成为多个组，True表示拆，False表示不拆
        skiprows    int,跳过多少行，一帮用于跳过前几行的描述性文字
        encoding    bytes,编码格式
"""


#排序
"""
    Numpy.sort(a,axis,kind,order)
        a   要排序的数组
        axis    使得sort函数可以沿着指定轴对数据集进行排序，axis = 1为沿横轴排序...axis = 0表示将数组平坦化之后进行排序
        kind    排序算法，默认为quicksort
        order   如果数组包含字段，则是要排序的字段
    argsort 和 lexsort函数
        可以在给定一个或多个键时，得到一个由整数构成的索引数组，索引值表示数据在新的序列中的位置
    unique函数 (去重)   结果会被排序
    tile(arr,3)     arr参数表示要重复的数组，3表示重复的次数为3
    repeat(a,reps,axis =None)   a表示需要重复的数组，reps是重复次数，axis = 0表示按行进行元素重复...
    
    统计函数std(求标准差),sum(求和),mean(求均值),min(),max(),var(方差)等
        **所有的统计函数在针对二维数组时都有轴的概念，axis = 0表示纵轴。
"""