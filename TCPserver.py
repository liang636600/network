import socket
import sys
import threading
import time

# 服务器处理一个tcp连接
def tcplink(sock, addr):
    print('服务器收到来自%s:%s的连接' % addr)
    # sock是服务器建立的与client连接的socket
    sock.send(b'Welcome!')
    while True:
        data = sock.recv(1024)
        time.sleep(1)
        if not data or data.decode('utf-8') == 'exit':
            break
        sock.send(('Hello, %s!' % data.decode('utf-8')).encode('utf-8'))
    sock.close()
    print('服务器与%s:%s的连接断开了' % addr)

serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 获取本地主机名
host = socket.gethostname()
# print('server主机名', host)
port = 9999

# 绑定主机和端口号
serversocket.bind((host, port))
# 设置最大挂起连接数
serversocket.listen(2)

while True:
    # 等待客户端连接
    clientsocket, addr = serversocket.accept()
    # 创建新线程来处理TCP连接:
    t = threading.Thread(target=tcplink, args=(clientsocket, addr))
    t.start()

    # print("连接地址: %s" % str(addr))

    # msg = '欢迎访问菜鸟教程！' + "\r\n"
    # clientsocket.send(msg.encode('utf-8'))
    # clientsocket.close()