from socket import *
from PIL import Image
import os
import time

serverName = "localhost" #Servidor local
serverPort = 12002 #Porta do servidor

buffer_size = 1024 #Tamanho do buffer indicado no projeto (1KB)

clientSocket = socket(AF_INET, SOCK_DGRAM) #Criação do socket, AF_INET indica uso do IPv4 e SOCK_DGRAM indica uso do UDP

files = os.listdir() #Lista de arquivos no diretório  
    
#Função para enviar arquivos, lendo o arquivo em binário e enviando-o em partes de tamanho buffer_size. Primeiro envia o nome do arquivo e depois o conteúdo

for file in files:
    if file.endswith('.txt') or file.endswith('.jpg'):
        clientSocket.sendto(file.encode(), (serverName, serverPort))  # Send filename
        with open(file, "rb") as f:  # Open file in binary mode
            dataFile = f.read()
            count=0
            for i in range(0, len(dataFile), buffer_size):
                count+=1
            count_bytes = count.to_bytes(4, byteorder='big')
            clientSocket.sendto(count_bytes, (serverName, serverPort))
            count = 0
            for i in range(0, len(dataFile), buffer_size):
                clientSocket.sendto(dataFile[i:i+buffer_size], (serverName, serverPort))  # Send file data
                count+=1
            print(count)
        break
 
# recebendo file modificada do servidor

modified_filename, serverAddress = clientSocket.recvfrom(buffer_size)
modified_filename = modified_filename.decode()

print(modified_filename)

if modified_filename == "udp_sent.jpg":  # Recebe a imagem
        
        time.sleep(2)        
        with open("udp_sent_back.jpg", 'wb') as arquivo2:
            for i in range(count):
                data, serverAddress = clientSocket.recvfrom(1024)
                if data:
                    arquivo2.write(data)
                else:
                    break

            print("Recebido")


else: # Recebe a o arquivo .txt
    for i in range(count):
        
        mc_part, serverAddress = clientSocket.recvfrom(buffer_size)
        with open("udp_sent_back.txt", "w") as arquivo:
            part = mc_part.decode()
            arquivo.write(part)
            print("Recebido pelo cliente")
            
    print(mc_part)
    
clientSocket.close() #Fechamento do socket