#导包import mulitprocessing
import multiprocessing,time,os
import threading


def coding(name,num):
    for i in range(1,num+1):
        time.sleep(0.2)
        print(f"{name}正在打第{i}遍代码！")
        #获取当前进程的pid
        print(multiprocessing.current_process().pid)
        print(f"当前进程的pid为：{os.getpid()}父进程pid为：{os.getppid()}")




#注意：
s  = ['aa','bb','bb','cc','bb',"bb",'bb','dd']

#for i in s: #这里s相当于['aa','bb','bb','cc','bb',"bb",'bb','dd']，没有和上面的s进行联系，所有s中的值的改变不会影响这个列表所有导致了错误
for i in s[:]:            #可以改为s[:],等价于对其进行了浅拷贝 copy.copy(s)由于这里只有一层的关系，所有即使进行深拷贝也是一样的效果，copy.deepcopy
    if i == 'bb':
        s.remove(i)
print(s)        #输出结果为['aa', 'cc', 'bb', 'bb', 'dd']并没有把所有的bb全部删除，这是因为：在循环时是对s字符串进行了硬拷贝


def music(name,num):
    for i in range(1,num+1):
        time.sleep(0.2)
        print(f"{name}正在唱第{i}次歌！")

print("我是main外资源")  #main外资源被所有的进程copy一份（main外资源不共享，不能真正意义上的去访问同一个对象）

"""
    设置当main进程结束是子进程也结束的两种方式：
        1.将子进程设置为守护进程(使用daemon)
        2.使用terminate手动关闭子进程，但是会让进程变成僵尸进程，后面会由python解释器自动回收（底层有init方法会进行管理)


"""

if __name__ == '__main__':
    code = multiprocessing.Process(target = coding,args = ("李白",10),name = '刘亦菲')    #更改进程名

    code.daemon = True      #设置为守护进程

    muc = multiprocessing.Process(target = music,args = ("爱困",10),daemon = True)

    code.start()
    muc.start()
    time.sleep(1)
    print("main内资源")