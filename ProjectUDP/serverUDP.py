from socket import *
import os
import time

# Mesma lógica do cliente, porém agora o servidor recebe o arquivo e o renomeia
serverPort = 12002
serverSocket = socket(AF_INET, SOCK_DGRAM)

buffer_size = 1024

serverSocket.bind(('', serverPort)) # Associa o socket a porta do servidor

print("The server is ready to receive")

# Função para receber arquivos, primeiro recebe o nome do arquivo e depois o conteúdo, além de renomear o arquivo
while True:
    filename, clientAddress = serverSocket.recvfrom(buffer_size)  # Recebe o nome do arquivo
    
    filename = filename.decode()
    
    print(type(filename))
        
    # recebe o numero da quantidade de envios
    count, clientAddress = serverSocket.recvfrom(4)
    count = int.from_bytes(count, byteorder='big')
        
    print(count)
        
    # faz *count* iterações para receber o arquivo
    file = b''
    for i in range(count):
        f, clientAddress = serverSocket.recvfrom(buffer_size)  # Recebe o conteúdo do arquivo
        file += f
        
    if filename == "udp_sending.txt":
        time.sleep(1)
        
        with open("udp_sent.txt", "w") as arquivo:
            part = file.decode()
            arquivo.write(part)
            print("Recebido")
        
        filename = "udp_sent.txt"
        
    elif filename == "udp_sending.jpg":
        time.sleep(1)

        with open("udp_sent.jpg", "w") as arquivo:
            arquivo.write(file)
            print("Recebido")
    
        
        filename = "udp_sent.jpg"
        
    # devolve o nome modificado para o cliente
    serverSocket.sendto(filename.encode(), clientAddress)
    
    if type(f) != bytes:
        file = file.encode() 
    
    # devolve a file para o cliente em *count* partes
    for i in range(count):
        start = i*1024
        serverSocket.sendto(file[start:start+buffer_size], clientAddress)
        
    print(file)
