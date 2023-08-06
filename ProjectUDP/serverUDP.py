from socket import *
from PIL import Image
import time

def receive_file(server_socket, buffer_size):
    filename, client_address = server_socket.recvfrom(buffer_size)
    filename = filename.decode()
    
    num_chunks, _ = server_socket.recvfrom(4)
    num_chunks = int.from_bytes(num_chunks, byteorder='big')
    
    data = b''
    for _ in range(num_chunks):
        chunk, _ = server_socket.recvfrom(buffer_size)
        data += chunk
    return filename, data, client_address

def send_back_file(server_socket, filename, data, client_address, buffer_size):
    with open(filename, 'rb') as f:
        for i in range(0, len(data), buffer_size):
            server_socket.sendto(data[i:i+buffer_size], client_address)
    print("Mandado de volta para o cliente")

server_port = 12002
buffer_size = 1024

server_socket = socket(AF_INET, SOCK_DGRAM)
server_socket.bind(('', server_port))

while True:
    quit = False
    while(1):    
        command = input('send/quit: ')
        if command == 'send':
            print("The server is ready to receive")
            break
        elif command == 'quit':
            quit = True
            break
        else:
            print('digite "send" para enviar um arquivo, ou "quit" para encerrar conexão')
    if quit: break
                  
    filename, data, client_address = receive_file(server_socket, buffer_size)

    if filename == "udp_sending.jpg":
        with open("udp_sent.jpg", 'wb') as file:
            file.write(data)
        with open("udp_sent.jpg", 'rb') as file:
            im = Image.open(file)
            im.show()
        send_back_file(server_socket, "udp_sent.jpg", data, client_address, buffer_size)
    elif filename == "udp_sending.txt":
        with open("udp_sent.txt", "w") as file:
            file.write(data.decode())
        data = data.decode().upper().encode()
        send_back_file(server_socket, "udp_sent.txt", data, client_address, buffer_size)

    server_socket.close()
