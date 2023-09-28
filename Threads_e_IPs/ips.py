import ipaddress #essa biblioteca imprime rede, faz cálculo com ip e possui outras funções.

"""Usei como exemplo o 192.168.0.0/32 por isso imprime apenas um ip. 
se fosse feito na terminação /24 ou /0 o resultado seria bem maior  """
ip = '192.168.0.0/32'

rede = ipaddress.ip_network(ip, strict=False) #strict vai desligar ele usando o False.

for ip in rede:
    print(rede)
