import socket



# Configurar o socket do cliente UDP
client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Usar diferentes endereços de IP e portas pro cliente e pro servidor(?)
host = '127.0.0.1'  # Endereço IP do servidor
porta = 12345       # Porta do servidor

while True:
    # Ajeitar a mensagem pra receber imagem e arquivo .txt
    mensagem = input("Digite a mensagem para o servidor (ou 'sair' para encerrar): ")
        
     # Enviar a mensagem para o servidor
    cliente_socket.sendto(mensagem.encode('utf-8'), (host, porta))

    # Encerrar o cliente se o usuário digitar "sair"
    if mensagem.lower() == 'sair':
        break

    # Receber e mostrar a resposta do servidor (opcional)
    resposta, endereco_servidor = cliente_socket.recvfrom(1024)
    print(f"Resposta do servidor: {resposta.decode('utf-8')}")

# Fechar o socket do cliente
cliente_socket.close()