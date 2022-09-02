import socket

HOST = '159.65.135.221'  
PORT = 2222
server_address = (HOST, PORT)

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
	s.connect(server_address)
	while True:
		data = s.recv(1024).decode("utf-8").split("\n")
		print(data[-2])
		xxx=data[-2].split()
		operations={"div":int(xxx[0])//int(xxx[2]),"mul":int(xxx[0])*int(xxx[2]),"add":int(xxx[0])+int(xxx[2]),"sub":int(xxx[0])-int(xxx[2])}
		if xxx[1] in operations:
			senddata=str(operations[xxx[1]])+"\n"
		else:
			print(data)
			break
		print(senddata)
		s.send(senddata.encode())
		
