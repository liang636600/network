# 导入 socket、sys 模块
import socket
import sys
import time

# 创建 socket 对象
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 获取目标主机名
targetHost = socket.gethostname()

# 设置目标端口号
targetPort = 9999

# 连接服务，指定主机和端口
s.connect((targetHost, targetPort))
# 客户端发送数据
print(s.recv(1024).decode('utf-8'))
for data in [b'Michael', b'Tracy', b'Sarah']:
    # 发送数据:
    time.sleep(5)
    s.send(data)
    print(s.recv(1024).decode('utf-8'))
# s.send(b'exit')
s.close()