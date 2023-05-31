import socket

host = "127.0.0.1"
port = 7002

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.connect((host, port))

while True:
    output = input("client: ")
    s.send(output.encode("utf-8"))
    if output == 'q': 
        break
    respond = s.recv(2048).decode("utf-8")
    print(f"server: {respond}")
    if respond == 'q':
        break
    

s.close()