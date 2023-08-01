import socket


# Configurar o socket do servidor UDP
server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
host = '127.0.0.1'  # Endereço IP do servidor
porta = 12345       # Porta que identifica o socket

# Vincular o socket ao endereço e porta
server_socket.bind((host, porta))
print("Servidor UDP esperando por mensagens...")

while True:
    # Receber os dados e o endereço do cliente
    dados, endereco_cliente = server_socket.recvfrom(1024)
    print(f"Mensagem recebida de {endereco_cliente}: {dados.decode('utf-8')}")

    # Responder ao cliente (opcional)
    resposta = "Mensagem recebida pelo servidor UDP."
    server_socket.sendto(resposta.encode('utf-8'), endereco_cliente)
