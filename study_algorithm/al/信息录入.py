
class students:
    def __init__(self,name,age,place):
        self.name=name
        self.age=age
        self.place=place
        print("你的信息是：")
print("请输入你的学生人数：")
number = input()

number = int (number)
for i in  range(0,number):
    print("input you are information:")
    name = input()
    age = input()
    place = input()
    student = students(name,age,place)
    print(f"当前第{i}位学生信息录入完成：")
    print(student.name)
    print(student.age)
    print(student.place)
