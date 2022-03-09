import socket

if __name__ == '__main__':
	HOST='localhost'
	port=12345
	sock=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	sock.connect((HOST, port))
	
	file=open("rec_test.txt","wb")
	file_data=sock.recv(1024)
	file.write(file_data)
	
	file.close()


