import socket
address = ('127.0.0.1', 3434)  # 服务端地址和端口
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

data ="Hello UDP!"
s.sendto(data.encode('utf-8'), address)

print("%s %s", data, address)

s.close()
