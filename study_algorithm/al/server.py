from socket import *
import cv2

s = socket()
# 223.160.115.186 实验对象
s.bind(('0.0.0.0', 8080))

s.listen()

conf, addr = s.accept()

print(addr)

# command = input('Enter command: ')
# conf.send(command.encode())
# while True:
#     file_size = int(conf.recv(1024).decode('utf-8'))  # 接受截图
#     conf.send('objk'.encode('utf-8'))
#
#     cur_size = 0
#     with open('2.png', 'wb') as f:
#         while cur_size < file_size:
#             data = conf.recv(2048)
#             f.write(data)
#             cur_size += len(data)  # 加上实际收到的
#     cv2.namedWindow("image")
#     img = cv2.imread('2.png')
#     cv2.imshow("image", img)
#     cv2.waitKey(10)
#
#
#




def send(fun):

    def fa():
        command = input('Enter command: ')
        while True:
            fun(command)
            text = conf.recv(1024).decode('utf-8')
            print(text)
            command = input('Enter command: ')
            if command == 'quit':
                break


    return fa
@send
def fun(command):
    conf.send(command.encode('utf-8'))

fun()