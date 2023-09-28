#Desenvolvimento de um cliente TCP
import socket, sys  #bibliotecas socket e sys sendo importadas

def main():
    try: #tentando uma conexão tcp/ip
        s = socket.socket(socket.AF_INET,socket.SOCK_STREAM,0) #usando o método socket.
        #AF_INET informa que ela corresponde a família TCP e SOCK_STREAM diz respeito ao IP
    except socket.error as e: #usando o método error da biblioteca socket,
        print("A coexão falhou!")
        print("Erro: {}".format(e))
        sys.exit() #vai sair do programa

    print("Socket criado com sucesso!")

    HostAlvo = input("Digite o Host ou IP a ser conectado:")
    PortaAlvo = input("Digite a porta a ser conectada")

    try:
        s.connect((HostAlvo,int(PortaAlvo))) #vai fazer a conexão
        print("Cliente TCP conectado com sucesso no Host" + HostAlvo + "e na Porta" + PortaAlvo)
        s.shutdown(2) #depois de 2 segundos fecha a conexão para evitar loop.
    except socket.error as e:
        print("Não foi possívle conectar ao Host: " +HostAlvo + " - Porta: "+ PortaAlvo)
        print("Erro: {}".format(e))
        sys.exit()
if __name__ == "__main__":  #se o nome for main chame o main"
    main()


'''Exemplo de teste bem sucedido:
Para o Host ou ip use: google.com.br 
Porta: 80

Exemplo de erro: (nesse caso a mensagem demora mais para ser exibida ,aguarde)
 Host ou ip: facebook.com.br
porta: 21

'''