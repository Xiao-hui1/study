import os,sys,threading,multiprocessing

mutex = threading.Lock()        #创建互斥锁

class PushBox:
    def __init__(self):
        self.myArray = []
    def read_data(self):
        mutex.acquire()         #启动锁
        with open('map.txt', 'w') as f:
            f.write("0,0,0,3,3,0,0\n")
            f.write("3,3,0,3,4,0,0\n")
            f.write("1,3,3,2,3,3,0\n")
            f.write("4,2,0,3,3,3,0\n")
            f.write("3,3,3,0,3,3,0\n")
            f.write("3,3,3,0,0,3,0\n")
            f.write("3,0,0,0,0,0,0\n")
            f.close()
        mutex.release()

    def read_file(self):
        while True:
            with open('map.txt', 'r') as f:
                data = f.readline()
                if not data:
                    f.close()
                    break
                else:
                    self.myArray.append(data)



import random
mutex2 = threading.Lock()

class GuessWord:
    def __init__(self):
        self.myArray = [
                        'hello','world','weapon','public','peculiar','abstract'
                        'illusion','legislation','conceal','estimate','associate'
                        ]
    def guess(self):
        mutex2.acquire()
        while True:
            num = random.randint(0,len(self.myArray)-1)
            print('word is:',"".join(random.sample(self.myArray[num],len(self.myArray[num]))))
            ges = input("Guess word: ")
            if ges == self.myArray[num]:
                print('Correct!')
            else:
                print('Incorrect!')
                print('Correct outcome is :',self.myArray[num])
            print('Whether you will continue or not.(Y/N):')
            condition = input()
            if condition == 'N' or condition == 'n':
                print('Goodbye!')
                break
        mutex2.release()


class Animal:       #定义抽象(abstract)类
    def speak(self):
        pass
#实现多继承
class Dog(Animal):
    def speak(self):
        print("I am a dog.")
class Cat(Animal):
    def speak(self):
        print("I am a cat.")
class Human(Animal):
    def speak(self):
        print("I am a human.")

class factory(Animal):
    def __init__(self,name):
        self.name = name
    def connect(self):
        if self.name == 'd':
            return Dog()
        elif self.name == 'c':
            return Cat()
        elif self.name == 'h':
            return Human()


if __name__ == '__main__':
    s = GuessWord()
    """
        在使用线程或则进程调用类里面的函数的时候，如果类中带有__init__魔术方法，必须在调用线程之前先对类进行声名调用，起对其中的魔术方法初始化的作用
        或者类中的类方法可能会出来typeerror，self错误:
        错误师范：  
            code = threading.Thread(target=GuessWord.guess).start()
            
    """
    code = threading.Thread(target=s.guess(),name='GuessWord',daemon=True).start()

    t = PushBox()
    read = threading.Thread(target=t.read_data,name='read_data',daemon=True).start()

    #code = multiprocessing.Process(target=s.guess(),name='GuessWord',daemon=True).start()
    # s = GuessWord()
    # s.guess()