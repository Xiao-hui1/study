# 用于练习python案例
# from importlib.metadata import pass_none
# from typing import Union
# from pymysql import connection
# 第一个案例：

#--------------------------------------------------------------------------------
#使用CTRL + D 可以将上一行的代码复制到下一行

class phone:

    __is_5g_enable = False        #私有属性同样不会被子类继承，且只能在内部被调用

    def __5g_check(self):         #私有方法不会被子类继承，只能在本类中被引用
        if self.__is_5g_enable:
            print("5g信号开启")
        else :
            print("5g信号关闭,使用4g信号")

    def call_by_5g(self):
        self.__5g_check()
        print("正在通话")
iphone = phone()
iphone.call_by_5g()

#第二个练习魔术方法：
class students:
    name = None
    age = None       # 注意魔术方法会自动调用     但前提是要有对应的魔术方法

    def __init__(self,name,age):
        self.name = name
        self.age = age
#输出信息
    def __str__(self):
        return f"{self.name} is {self.age} years old"
#小于比较
    def __lt__(self,other):
        return self.age < other.age
#大于比较
    def __gt__(self,other):
        return self.age > other.age
#等于比较
    def __eq__(self,other):
        return self.age == other.age
stu1 =  students("周杰伦",32)

stu2 = students("林俊杰",28)

print(stu1>stu2)
print(stu2<stu1)
print(stu1==stu2)
print(stu1)
print(stu2)


print('-'*64)
# 第三个案例父类的继承
#子类不能直接继承父类中的私有变量，但是父类的私有变量仍然会被存放在子类中，可以使用self._父类名__方法名  来进行访问。

class Phone:
    producer = "itheima"
    # def __init__(self,name):
    #     self.name = name
    @classmethod
    def call_by_5g(cls):
        print(cls.producer)
        print("5g信号已开启；")

class call:
  def call(self):
    print('call')

#多继承
class My_Phone(Phone,call): #从左往右继承，在前面没有的情况就会先后寻找
    producer :str = "Asus"
    number :int = 5
    my_name = ["wangyan", 1, "tiancai"]
    # def __init__(self,name):
    #     Phone.__init__(self,name)     #调用基类

    def call_by_5g(self) -> None:
        print("5g信号已开启，通话正在进行；") #type: str
        print(f"您的产品是：{Phone.producer}")
        super().call_by_5g() #type: Phone     #在子类中重新调用父类的变量或函数

print(issubclass(My_Phone,Phone))   #判断My_Phone 是否为Phone的派生类
b = Phone()

print(isinstance(b,Phone))      #判断b是否为Phone的类对象
phone = My_Phone()
phone.call_by_5g()      #type: Phone

#多态
# class Animal:
#     def speak(self):
#         pass
# class Dog(Animal):
#     def speak(self):
#         print("汪汪汪")
# class Cat(Animal):
#     def speak(self):
#         print("喵喵喵")
#
# def speak(animal):
#     animal.speak()
#
# cat = Cat()
# dog = Dog()
# speak(cat)
# speak(dog)

#使用MySQL数据库
# conn =  connection(
#     host = 'localhost',
#     port = 3306,
#     user = 'root',
#     password = '060438'
# )
# print(conn)
# conn.close()
# class Solution:
#     def reverse(self, x :int) ->int:
#         num = 0
#         falg = 0
#         if x<0 :
#             x *=-1
#             falg = 1
#         while x>0:
#             y = x%10
#             x = x//10
#             num = num*10 + y
#         if falg:
#             return num*-1
#         else:
#             return num
#
# st = Solution()
# s = st.reverse(321)
# print(s)



#__dict__方法              #使用**dict方法可以将字典再转换回原来的样子
#可以把对象的属性名作为字典的 key，吧对象的属性值作为字典的 value;
#列如L:
# class student(object):
#     def __init__(self, name, age, call, address):
#         self.name = name
#         self.age = age
#         self.call = call
#         self.address = address
# st = student('dehua',13,12345,'hunning')
# my_dict = st.__dict__
# print(my_dict)


#元组，集合，整数，字符串都属于不可变类型，如果直接改变其值则回报错TypeError
# s = "world"
# #
# # s[2] = chr(ord(s[2])-32)
# #
# # print(s)
# # 要改变其值可以先使用类型转换成可变类型后在进行修改
#
# l = list(s)
#
# l[2] = chr(ord(l[2])-32)
#
# l = ''.join(l)      #将一个可迭代对象转换成一个字符串，前面的表示连接的分隔符
#
# s = ['world','legislation','peculiar','margin','weapon']
#
# s = ' '.join(s)     #将s连接成为一个整体，以空格分开
# print(s)
# print(l)
#
#
# number = 3.1415926
# print(f"{number:.3f}")      #保留小数位数的方式
str = [1,3,3]
print(*str) #一次性输出str的所有内容，以空格隔开
"""
    导入copy模块可以实现深浅拷贝
    对于不可变类型,深浅拷贝等同于直接赋值没有实际意义
    对于可变类型,浅拷贝会将第一次拷贝一次,即将copy的对象的值原封不动的复制一遍;
    而深拷贝的时候会拷贝到底会将其中的内容的值全部copy过来
        例如:
            a = [1,2,3]
            b = [4,5,6]
            c = [7,8,9,a,b]
            import copy
            d = copy.deepcopy(c)       即修改了a,b列表中的值不会影响到d的内容
            print(c)   #input: 7 8 9 1 2 3 4 5 6

"""


