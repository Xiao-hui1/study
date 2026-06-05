"""
    可以把函数当作属性使用，
    目的是简化代码。
    实现方式：
        1.使用装饰器
            @property       修饰  获取值的函数
            @获取值的函数名.setter     修饰  设置值的函数
        2.使用类属性

"""
class Student:
    def __init__(self):
        self.__age = 0
        self.__id = 0

    @property
    def age(self):
        return self.__age
    @property
    def id(self):
        return self.__id
    @id.setter
    def id(self,id):
        self.__id = id

    @age.setter
    def age(self, age):
        self.__age = age





"""
    使用类来定义

    class Student:
        def __init__(self):
            self.__age = 18
        
        def get_age(self):
            return self.__age
        
        def set_age(self, age):
            self.__age = age
        
        age = property(get_age, set_age)    注意这里的 参数1：获取的函数名，参数2：设置值的函数名
        
        
    和上面同一效果
"""



if __name__ == '__main__':
    s = Student()
    s.age = 20
    s.id = 25678996
    print(s.age, s.id)
