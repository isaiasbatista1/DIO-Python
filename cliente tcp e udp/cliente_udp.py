import socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) #SOCK_DGRAM é o protocolo de datagrama do usuário.

print('Cliente Socket criado com sucesso!')

host = 'localhost'
porta = 5433  #porta que ele vai se conectar no servidor
mensagem = "Iai Servidor, tudo jóia?"

try:
    s.sendto(mensagem.encode(), (host, 5432))#encode empacota os dados. #5432 é a porta do servidor

    dados, servidor = s.recvfrom(4096) #vão esperar uma resposta de 4096bytes
    dados = dados.decode() #decode desempacota os dados.
    print('Cliente: ' + dados)
finally:
    print('Cliente: Fechando a Conexão')
    s.close()
