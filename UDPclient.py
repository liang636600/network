import socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
for data in [b'Michael', b'Tracy', b'Sarah']:
    # 发送数据:
    s.sendto(data, (socket.gethostname(), 9999))
    # 接收数据:
    print('客户端收到服务器的数据',s.recv(1024).decode('utf-8'))
s.close()