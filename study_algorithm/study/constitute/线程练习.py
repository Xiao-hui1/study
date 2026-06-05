#导包：
import threading,time
"""
        线程直接共享全局变量

"""


# myList = []
#
# def worker():
#     for i in range(1,11):
#         myList.append(i)
#         print(f"这是我的第{i}份工作了！")
#
# def reading():
#     print(myList)


"""
    在多个线程共享资源的时候可能会出现我们意想不到的结果，多个线程在相互抢夺资源，导致最终两个结果都出现错误
    解决办法是：采用互斥锁，给线程上锁在一个线程，没有走完是另一个不会去抢资源
    格式：
    创建锁：
    mutex = threading.Lock()            注意这里的 Lock 是一个类
    启动锁：
    mutex.acquire()
    释放锁：
    mutex.release()
    
    如果没有释放锁，则会出现死锁的情况，即一直在一个线程里面无法向下继续执行了
"""



mutex = threading.Lock()
#mutex2 = threading.Lock()   #使用两把锁回导致锁不住的情况

global_num = 0      #定义全局变量

def num_fun1():
    global global_num    #声名全局变量
    mutex.acquire()
    for i in range(1000000):
        global_num += 1
    print("function1",global_num)
    mutex.release()


def num_fun2():
    global global_num
    #mutex2.acquire()

    mutex.acquire()
    for i in range(1000000):
        global_num += 1
    print(global_num)

    mutex.release()

    #mutex2.release()
# class Mutex:
    # def __init__(self):
    #     self.lock = threading.Lock()
    #     self.mutex = threading.Lock()
    # def first(self):
    #     self.lock.acquire()
    #     print("first")
    #     self.lock.release()
    # def second(self):
    #     time.sleep(1)
    #     self.mutex.acquire()
    #     print("second")
    #     self.mutex.release()
    # def third(self):
    #     time.sleep(2)
    #     print("third")
if __name__ == '__main__':

    n1 = threading.Thread(target=num_fun1)
    n2 = threading.Thread(target=num_fun2)
    n1.start()
    n2.start()
    # t = threading.Thread(target=worker,daemon=True) #线程中也用守护模式，但是没有terminate()
    # t1 = threading.Thread(target=reading)
    # t.start()
    # t1.start()
    # print('main over!')