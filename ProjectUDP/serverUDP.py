from socket import *
import os
import time

# Mesma lógica do cliente, porém agora o servidor recebe o arquivo e o renomeia
serverPort = 12000
serverSocket = socket(AF_INET, SOCK_DGRAM)

buffer_size = 1024

serverSocket.bind(('', serverPort)) # Associa o socket a porta do servidor

print("The server is ready to receive")

# Função para receber arquivos, primeiro recebe o nome do arquivo e depois o conteúdo, além de renomear o arquivo
while True:
    filename, clientAddress = serverSocket.recvfrom(buffer_size)  # Recebe o nome do arquivo
    filename = filename.decode()
    if filename == "udp_sending.txt":
        time.sleep(1)
        os.rename("udp_sending.txt", "udp_sent.txt")
        filename = "udp_sent.txt"
    elif filename == "udp_sending.jpg":
        time.sleep(1)
        os.rename("udp_sending.jpg", "udp_sent.jpg")
        filename = "udp_sent.jpg"
    while True:
        f, clientAddress = serverSocket.recvfrom(buffer_size)  # Recebe o conteúdo do arquivo
        if filename.endswith('.txt'):
            f = f.decode()
            
            # modificando conteúdo da file ('.upper()' em caso de file '.txt')
            
            f = f.upper()
            
            with open(filename, 'w') as file:
                file.write(f)
                break
            
    serverSocket.sendto(filename.encode(), clientAddress)
    
    if type(f) != bytes:
        f = f.encode() 
        
    for i in range(0, len(f), buffer_size):
                serverSocket.sendto(f[i:i+buffer_size], clientAddress)