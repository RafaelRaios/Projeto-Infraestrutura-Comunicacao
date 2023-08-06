from socket import *
from PIL import Image
import os
import time

def send_file(client_socket, filename, server_address, buffer_size):
    client_socket.sendto(filename.encode(), server_address)  # Send filename
    with open(filename, "rb") as f:
        data_file = f.read()
        num_chunks = len(data_file) // buffer_size + (len(data_file) % buffer_size != 0)
        client_socket.sendto(num_chunks.to_bytes(4, byteorder='big'), server_address)
        
        for i in range(0, len(data_file), buffer_size):
            client_socket.sendto(data_file[i:i+buffer_size], server_address)  # Send file data
    return num_chunks

def receive_modified_file(client_socket, original_filename, buffer_size, num_chunks):
    print(f"Esperando {num_chunks} partes do servidor...")
    if original_filename.endswith('.jpg'):
        expected_filename = "udp_sent_back.jpg"
        with open(expected_filename, 'wb') as file:
            for _ in range(num_chunks):
                data, _ = client_socket.recvfrom(buffer_size)
                file.write(data)

        print("Recebido")
        with open(expected_filename, 'rb') as file:
            im = Image.open(file)
            im.show()
    else:
        expected_filename = "udp_sent_back.txt"
        received_text = ''
        for _ in range(num_chunks):
            data, _ = client_socket.recvfrom(buffer_size)
            received_text += data.decode()

        with open(expected_filename, 'w') as file:
            file.write(received_text)
        print("Recebido pelo cliente")

server_name = "localhost"
server_port = 12002
buffer_size = 1024

client_socket = socket(AF_INET, SOCK_DGRAM)

files = os.listdir()

for file in files:
    if file.endswith('.txt') or file.endswith('.jpg'):
        num_chunks_sent = send_file(client_socket, file, (server_name, server_port), buffer_size)
        receive_modified_file(client_socket, file, buffer_size, num_chunks_sent)
        break

client_socket.close()