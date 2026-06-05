""""
    namedtuple()    创建具有命名字段的元组子类
    deque           两端都带有快速追加和弹出的队列
    ChainMap        用类俩创建多个映射的单个视图
    Counter         用于计算可哈希对象的字典子类
    OrderedDict     保持元素顺序的字典子类
    defaultdict     调用函数来提供缺少的值的字典子类
    UserDict、UserList、UserString    这三种数据类型只是它们的底层基类的包装器。
    它们的使用在很大程度上已经被直接子类话它们各自基类的能力所取代。可用于访问基础对象作为属性
"""
import collections
import itertools, array, sys, os
from collections import *

dp = deque('abc')

dp.append('d')
dp.append('e')

dp.extend('syt')

dp.extendleft('yxw')    #注意在队列里面的顺序为：'w', 'x', 'y'

print(dp)

dp.rotate(2)        #让队列进行旋转

dp.rotate(-1)
print(dp)

print('-'*64)

print("队列的切片：")
print(list(itertools.islice(dp,3,9)))


dp2 = deque([],maxlen=3)    #给队列设置一个固定的大小，非常适用于循环缓冲的数据结构。

for i in range(6):
    dp2.append(i)
    print(dp2)



#-------------------------------------------------------------------------------------

print('\ntest ChainMap:','-'*32)
dict1 = {'a':1,'d':2,'c':3}
dict2 = {'d':1,'f':2,'e':3}

chainmap = ChainMap(dict1, dict2)
print(chainmap)
print(chainmap.maps)

print(chainmap['d'])

print(chainmap.values())

chainmap.new_child({'d':3})
chainmap.pop('d')

print(chainmap.parents)





#-----------------------------------------------------------------------------------------
#Counter 和 dictionary之间最显著的区别是，Counter为丢失的项返回记零数，而不会引发错误。
print('test Counter','-'*32)
#统计出现的次数
counter = Counter('foundation')
print(counter)

c = Counter({'a':2,'b':3,'c':4})
c1 = Counter(a=1,b=1,c=1)
c.update({'a':2,'c':5})         #updata功能是把新值累加进去，而非替换
c.subtract({'b':2})         #减去值，与updata相反。
print(c)
print(c1)

print(sorted(c.elements()))     #创建一个迭代器

print(c.most_common())  #最大输出多少项，省略为全部输出

print('\nOrderedDict:','-'*42)




#-----------------------------------------------------------------------------------------
#OrderedDict()与普通字典不同的是，普通字典的插入顺序不影响，字典的比较，而OrderDict如果插入的顺序不同则会返回False
d = collections.OrderedDict([('a',1),('b',2),('c',3)])
d1 = collections.OrderedDict([('a',1),('c',3),('b',2)])

print(d==d1)

#defaultdict
dd = collections.defaultdict(int)
words = 'blue green green white pink red red gery yellow'.split()
for w in words:
    dd[w] += 1
print(dd)

print("\nnamedtuple--------------------------------------------")





#-----------------------------------------------------------------------------------------------
#namedtuple     命名元组

space = namedtuple('space','a x y')

s = space(3,4,2)
print(s)
print(s.a * s.x * s.y)

print(s._asdict())      #test _asdict()

s1 = [3,4,5]
print(space._make(s1))

print(space._make(s1)._replace(a=0,x=1))    #更改命名元组中的值
print(space._fields)    #输出字段名称的字符元组





#----------------------------------------------------------------------
print('array test module: ','-'*32)

test = array.array('i',range(10**6))

test1 = list(range(10**6))

print(sys.getsizeof(test)/sys.getsizeof(test1))         #可以看到使用array模块创建数组所占用的内存空间小很多