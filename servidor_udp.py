import socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

print("Socket Criado com sucesso")

host = 'localhost'
port = 5432


s.bind((host,port)) #vai fazer a ligação entre cliente-servidor entre o host e a porta
mensagem = '\nServidor: Opaaaa,recebi sua mensagem. Aqui está tudo bem!'

while 1:
    dados, end = s.recvfrom(4096) #end = endereço

    if dados:
        print('Servidor enviando mensagem... ')
        s.sendto(dados + (mensagem.encode()), end)