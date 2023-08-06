# Projeto de Infra-Estrutura de Comunicação 2023.1

## Entrega 1: Transmissão de arquivos com UDP

- A estrutura do projeto conta com 2 diretórios principais para a primeira parte: ```ProjectUDP``` e ```TestFiles```
- Dentro do diretório ```ProjectUDP``` conta o arquivo ```clientUDP.py``` e ```serverUDP.py```, sendo o cliente e servidor do projeto com UDP, respectivamente

### Testando o Projeto
- Primeiro, mova algum dos arquivos (apenas um) de imagem ou texto para o diretório do projeto UDP, manualmente ou utilizando o comando ```mv TestFiles/udp_sending.txt ProjectUDP``` no terminal (para mover o arquivo de imagem, basta trocar .txt por .jpg)
- Certifique-se de ter alguma versão do python instalada na sua máquina. Como exemplo, usaremos o python3.x.x
- Entre no terminal no diretório principal utilizando ```cd ProjectUDP/``` e em seguida execute os seguintes comandos (em ordem!) em terminais diferentes para melhor visualização:
    - ```python3 serverUDP.py``` => Para enviar um arquivo/iniciar a conexão, digite 'send' no terminal do servidor. Para encerrar a conexão, digite 'quit'.
    - ```python3 clientUDP.py```
- Caso tenha escolhido o arquivo texto, além da modificação de nome do arquivo, também sera mostrado o conteúdo do mesmo
- A imagem possui um tamanho maior, para demonstrar que caso o arquivo seja maior que o buffer, seja mandado em partes para o servidor e em seguida retornado
#
