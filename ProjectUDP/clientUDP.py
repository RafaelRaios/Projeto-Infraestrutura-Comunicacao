from socket import *
import os

serverName = "localhost" #Servidor local
serverPort = 12000 #Porta do servidor

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
                clientSocket.sendto(dataFile[i:i+buffer_size], (serverName, serverPort))  # Send file data
                count+=1
            print(count)
        break

    
# recebendo file modificada do servidor

modified_filename, serverAddress = clientSocket.recvfrom(buffer_size)
modified_filename = modified_filename.decode()

print(modified_filename)

# recebe (em *count* partes) o arquivo modificado
for i in range(count):
    mc_part, serverAddress = clientSocket.recvfrom(buffer_size)
    print(mc_part)
