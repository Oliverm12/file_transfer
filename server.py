import socket
import sys

if __name__ == '__main__':
	sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	server_address = ('localhost',12345)
	sock.bind(server_address)
	sock.listen(1)
	conn, addr = sock.accept()

	file = open("test.txt", "rb")
	file_data = file.read(1024)
	conn.send(file_data)

