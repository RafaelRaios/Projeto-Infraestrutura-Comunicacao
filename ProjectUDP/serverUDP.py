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
    
    if filename == "udp_sending.txt":
        time.sleep(1)
        os.rename("udp_sending.txt", "udp_sent.txt")
        filename = "udp_sent.txt"
    elif filename == "udp_sending.jpg":
        time.sleep(1)
        os.rename("udp_sending.jpg", "udp_sent.jpg")
        filename = "udp_sent.jpg"
        
    # verifica o numero de envios necessarios, levando em consideracao
    # o tamanho do buffer
    with open(filename, 'rb') as file:
        content = file.read()
        count = (len(content)//buffer_size) + 1
        
    print(count)
        
    # faz *count* iterações para receber o arquivo
    for i in range(count):
        f, clientAddress = serverSocket.recvfrom(buffer_size)  # Recebe o conteúdo do arquivo
        if filename.endswith('.txt'):
            f = f.decode()
            
            # modificando conteúdo da file ('.upper()' em caso de file '.txt')
            
            f = f.upper()
            
            with open(filename, 'w') as file:
                file.write(f)
                break
    
    # devolve o nome modificado para o cliente
    serverSocket.sendto(filename.encode(), clientAddress)
    
    if type(f) != bytes:
        f = f.encode() 
    
    # devolve a file para o cliente em *count* partes
    for i in range(count):
        serverSocket.sendto(f[i:i+buffer_size], clientAddress)
    break

serverSocket.close() #Fechamento do socket