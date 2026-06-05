def f(time):
    def outer(fun):

        #nonlocal time 关键字可以使内部函数可以修改外部变量
        def inner(*args, **kwargs): #带参数的装饰器
            result = []
            print("我要睡觉了")
            result = fun(*args, **kwargs)
            print("我睡醒了")
            print(result)
        return inner
    return outer


@f(time = 3)     #带参数的装饰器，不需要带参数则只需要嵌套两层
def sleep(name):
    import random , time
    print(f"{name}正在睡觉·····")
    time.sleep(random.randint(1,5))


sleep("libai")



#单列模式
class StrTools:
    pass

strtools = StrTools()

#在另外一个python代码里面调用strtools变量（不是StrTools类）就可以得到一个单列模式了，调用单列模式时所使用的地址空间永远是同一个空间


#工厂模式
class Person:
    pass
class Student(Person):
    pass
class Teacher(Person):
    pass
class worker(Person):
    pass

class factory(Person):
    def get_person(self,p_type):
        if p_type == 's':
            return Student()
        elif p_type == 't':
            return Teacher()
        elif p_type == 'w':
            return worker()

pf = factory()
work = pf.get_person('w')
stu = pf.get_person('s')
teacher = pf.get_person('t')


