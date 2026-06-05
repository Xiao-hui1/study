"""
    s.capitalize()  返回一个包含第一个字符的字符串大写，其余都是小写的
    s.count(substring,[start,end])  统计其中的子串出现的次数
    s.expandtabs([tabsize]) 用空格代替制表符
    s.endswith(substring)   是否以子串结尾
    s.startswith(substring)  是否以子串开始
    s.find(substring,[start,end))   放回字符串第一次出现的索引位置
    s.isalnum() 如果所有的字符都是字母数字，则放回true
    s.isalpha()如果所有的字符都是字母顺序排列的，则放回true
    s.isdigit() 如果所有的字符都是数字，则放回true
    s.split([separator],[maxsplit]) #maxsplit 最大允许分割的次数
    s.join(t) 连接序列中的字符串
    s.replace()
    s.swapcase()    返回字符串的副本，并在字符串中大小写交换
    s.strip()
    s.lstrip([characters])  返回字符串的副本，并删除左侧的指定字符

"""

s = 'hello world'
print(s.swapcase())
print(s.split(' ',1))

di = ['2','3','4','5','6','7','8','9']
print(list(map(int,di)))

print(list(filter(lambda x : int(x)%2 == 0,di)))
di = [1,2,3,4,5,6,7,8,9]

'''复数   (complex)   f.real读取实部      f.imag  读取虚部'''
f = 5 + 3j
print(f)
print(f.real)
print(f.imag)

print('-'*64)

import  decimal

x = decimal.Decimal(2.76)
y = decimal.Decimal(1.34)

print(x*y)

decimal.getcontext().prec = 4   #设置精度

print(x*y)          #print3.698
print(1.34*2.76)    #print3.6984

"""
    x.exp() 自然指数
    x.ln()  自然对数
    x.log10()
    
    fractions   有理数类型的
"""

import fractions
print(fractions.Fraction(2, 3))     #print 2/3
print(fractions.Fraction(0.5))  # print 1/2



'''
    字典方法：
        d.clear()
        d.copy()
        d.fromkeys(s[,value])   返回一个新的字典，其中的键来自s序列的和
        d.get(k[,v])    日了狗找到返回d[k],否则返回v,v没有指定则返回None
        d.items()   返回字典d的所有键/值对
        d.keys()    返回字典中的所有键d
        d.pop(k[,default])  返回d[k]并且删除它
        d.popitem() 从字典中随机删除一个键值对，并以元组的形式返回
        d.setdefault(k,[,v])    返回d[k],如果没有找到，则返回v并将d[k]设置为v
        d.updata()
        d.values()  返回字典中的所有对象
'''

c = dict(zip(['a','b','c'],[3,1,9]))    #利用zip创建字典。
c.update({'d':6,'e':5})

d  = [x for x in sorted(c.values(),reverse=True)]       #按字典的值进行排序
c = [c[x] for x in sorted(c,key = c.__getitem__,reverse=True)]  #同上

print(d)
print(c)
