from socket import *
from PIL import Image
import time

# Mesma lógica do cliente, porém agora o servidor recebe o arquivo e o renomeia
serverPort = 12002
serverSocket = socket(AF_INET, SOCK_DGRAM)
serverName = "localhost"

buffer_size = 1024

serverSocket.bind(('', serverPort)) # Associa o socket a porta do servidor

# Função para receber arquivos, primeiro recebe o nome do arquivo e depois o conteúdo, além de renomear o arquivo
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
    
    filename, clientAddress = serverSocket.recvfrom(buffer_size)  # Recebe o nome do arquivo
    
    filename = filename.decode()
    
    print(type(filename))
        
    # recebe o numero da quantidade de envios
    count, clientAddress = serverSocket.recvfrom(4)
    count = int.from_bytes(count, byteorder='big')
        
    print(count)
        
    # faz count iterações para receber o arquivo
    file = b''
    if filename == "udp_sending.jpg":
        time.sleep(2) 
        filename = "udp_sent.jpg"     
        with open("udp_sent.jpg", 'wb') as arquivo:
            
            for i in range(count):
                data, clientAddress = serverSocket.recvfrom(1024)
                if data:
                    
                    arquivo.write(data)
                    #data, clientAddress = serverSocket.recvfrom(1024)
                else:
                    break

            print("Recebido")
        
    else:
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
        
    # devolve o nome modificado para o cliente
    serverSocket.sendto(filename.encode(), clientAddress)

    # Devolve a imagem para  o cliente
    if filename == "udp_sent.jpg":
        
        with open("udp_sent.jpg", 'rb') as f:
            dataFile = f.read()
            count = 0
            for i in range(0, len(dataFile), buffer_size):
                serverSocket.sendto(dataFile[i:i+buffer_size], clientAddress)  # Send back image
                count+=1
            print("Enviado")
    
    # devolve o arquivo texto para o cliente
    else:
        file = file.decode().upper().encode()  # Convert the text to uppercase
        for i in range(count):
            start = i*1024
            serverSocket.sendto(file[start:start+buffer_size], clientAddress)

serverSocket.close() # Fecha o socket