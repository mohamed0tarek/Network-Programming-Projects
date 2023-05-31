import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = "127.0.0.1"
port = 7002

s.bind((host, port))
s.listen(5)
client, address = s.accept()
print("connection from ", address[0])

while True:
    respond = client.recv(2048).decode("utf-8")
    print(f"client: {respond}")
    if respond == 'q':
        break
    output = input("server: ")
    client.send(output.encode("utf-8"))
    if output == 'q':
        break

client.close()
