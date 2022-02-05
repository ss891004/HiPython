import socket
address = ('127.0.0.1', 31500)  # 服务端地址和端口
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind(address)  # 绑定服务端地址和端口

while True:
    data, addr = s.recvfrom(1024)  # 返回数据和接入连接的（客户端）地址

    print("Received: %s from %s" % (data, str(addr)))

s.close()
