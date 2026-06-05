"""
    pandas的三大数据结构：
        series  类似数组
        DataFrame   类似表格
        Panel       类似excel的多表单Sheet
"""
from operator import index
import numpy as np
import pandas as pd
obj = pd.Series([1,-2,3,-4])

print(obj)  #输出的第一列为index索引，第二列为数组值

print('-'*64)

i = ['a','b','c']
v = [1,2,3]
val = pd.Series(v,index=i,name='value')
print(val)
print(val['a'])
print(val.index)

a = {'a':1,'b':2,'c':3}
v = pd.Series(a)
#当键值没有匹配项时会出现NaN(not a number)
let = ['d','b','c','a']
st = pd.Series(v,index = let)
print(st+v)     #不同索引的自动对齐
v.index = ['b','c','d']     #修改index

data = {
    'name':['Alex','Bob','C'],
    'age':[21,22,23],
    'year':[23,25,26],
}

df = pd.DataFrame(data)     #全部列会被有序排列，如果指定了列名序列，则DataFrame的列就会按照指定顺序进行排列
d = pd.DataFrame(data,columns=['name','year','age'])
print(d)
print(df)

print('-'*64)
"""
    DataFrame 的常用属性：
        values      获取元素
        index       获取索引
        columns     列名
        dtypes      类型
        ndim        维度
        shape       形状
        size        个数
    当重建索引引入的缺失值可以用fill_value参数填充
"""
dp = pd.Series([1,2,3,4,5],index=['a','b','c','d','e'])
print(dp)
print(dp.reindex(['a','b','c','d','e','f'],fill_value=0))
print(dp.reindex(['a','b','c','d','e'],method='pad'))   #缺失值时的填充，pad或ffill 表示先前值填充，bfill或backfill表示向后

print('-'*64)
#更换索引：
df = d.set_index('name')    #将列数据作为索引
df = d.reset_index()    #将索引作为列数据
print(df['year'])

"""
    head()  获取前五行默认，带值则为前n行
    tail()  获取后五行...
    sample(n)   随机抽取n行显示
    loc(行索引位置，列索引位置)
    iloc([行索引下标],[列索引下标])   ：df.iloc([1,2],[1,3])   显示第1行和第2行，与每一行的的第1列和第3列元素。
    ix()    支持上面的两种方式，可以用混合使用   例如：ix.(1:3,['name','year'])
"""
print('-'*64)

values = df[df['year']==23]     #对数据进行布尔选择
print(values)

#--------------------------------------------------------------------

"""
            数据修改是直接对DataFrame进行修改，无法撤销。
"""
#增加一行数据
data = {
    'name':['Alex','Bob','C'],
    'age':[21,22,23],
    'year':[23,25,26]
}
df = pd.DataFrame(data,index=['A','B','C'])
data2 = {'name':'Luca','age':18,'year':24,'city':'hunan'}
# df1 = df._append(data2,ignore_index=True)
# df1['age'] = 18
# df1['province'] = 'Beijing'     #添加列
# print('-'*64)
print(df.drop(columns=['age']))       #删除列  或   df.drop('age',axis = 1,inplace = True)
print(df.drop('B'))     #删除指定索引值的那行，如果该行不存在则报错。
print('-'*64)


"""
        算数运算：
            相同索引的数据会相加，如果没有匹配的索引不会保留之前的值，而是变成缺失值（NaN）
"""
#Series相加
obj1 = pd.Series([1,2,3],index=['A','B','C'])
obj2 = pd.Series([1,2,3],index=['A','D','C'])
print(obj1+obj2)

#DataFrame相加：
a = pd.DataFrame(np.arange(6).reshape(2,3),index=['A','B'],columns=['a','b','c'])
b = pd.DataFrame(np.arange(4).reshape(2,2),index=['A','D'],columns=['a','b'])
print(a+b)

"""
    函数的应用与映射：
        map()   将函数套接到Series的每个元素中
        apply() 将函数套接到DataFrame的行与列中，行列用axis参数设置
        applymap()  将函数套用DataFrame的每个元素上
"""
print('-'*64)
data = {
    'name':['Alex','Bob','C'],
    'age':[21,22,23],
    'price':['23元','34元','78元']
}
te = pd.DataFrame(data)
def f(x):
    return x.split('元')[0]
te['price'] = te['price'].map(f)
print(te)

print('-'*64,"apply:")

data =  pd.DataFrame(np.random.randn(4,4),index=['app','win','peer','diplomat'],columns=['A','B','C','D'])
print(data.apply(np.mean))

print('-'*64,"applymap:")
print(data.applymap(lambda x: '%.3f' % x))
print('-'*64,"排序：")

"""
    排序：
        sort_index  函数方法对索引进行默认排序，默认为升序，使用ascending = False 改为降序
        sort_values 对值进行排序  对于Dataframe数据则需要家by = ''  对对应的数据进行排序。
        sum 汇总函数
        describe    对灭国数值型列进行统计
"""

wy  = pd.Series([1,2,3],index=['A','B','C'])
print(wy.sort_index(ascending=False))
print(data.sort_values(by = 'A'))
print(data.sum(axis=1))     #行
print(data.sum())           #按列进行汇总
print('-'*64)

print(data.describe())

obj = pd.Series([1,2,3,4,6,3,2,5])
print(obj.unique())     #频数统计
print(obj.value_counts())       #会按频数排序

"""
    数据分组与聚合：
        groupby     可以根据索引或字段对数据进行分组
            format:
                DataFrame.groupby(by=None,axis = 0,level = None ,as_index = True,sort = True, group_keys = True, squeeze = False)
            by :可以传入函数，字典，Series等，用于确定分组依据
            axis    接收int，表示操作的轴方向，默认为0
            level   接收int或索引名，代表标签所在的级别，默认为None
            as_index    接收boolean,表示聚合后的标签是否以DataFrame索引输出
            sort    接收Boolean，表示对分组依据和分组标签排序，默认为True
            group_keys  接收boolean，表示是否显示分组标签的名称，默认为True
            squeeze     接收Boolean,表示是否允许情况下对返回数据降维，默认为False
"""

df = pd.DataFrame({'key1':['a','a','b','b','a'],'key2':['yes','no','yes','yes','no'],'data1':[1,2,3,4,5],'data2':[1,2,3,4,5]})
group1 = df['data1'].groupby(df['key1'])
print(group1.size())
print(df.groupby('key2').sum())     #以列索引名称作为分组键

wlist = ['w','w','y','y','w']

#分组键可以是长度和DataFrame行数相等的列表或元组，相当于将列表或元组看作DataFrame的一列，然后分组
print(df.groupby(wlist).sum())

#按字典分组：
df = pd.DataFrame(np.random.normal(size = (6,5)),index=['A','B','a','c','C','b'])
wdict = {'a':'one','b':'two','c':'three','A':'one','B':'two','C':'three'}
print(df.groupby(wdict).sum())
print('-'*64)

