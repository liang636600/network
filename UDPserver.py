import socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# 绑定端口:
s.bind((socket.gethostname(), 9999))

print('Bind UDP on 9999...')
while True:
    # 接收数据:
    data, addr = s.recvfrom(1024)
    print('服务器收到从%s:%s来的数据' % addr)
    s.sendto(b'Hello, %s!' % data, addr)