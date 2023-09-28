import os #Importa o módulo ou biblioteca os (Integra os programas e
#recursos do S.O

print('#' * 60)#Imprimindo  #60 vezes

#criamos uma variavel que vai receber do usuário um ip
ip_ou_host = input("Digite o IP`ou Host a ser verificado: ")

#chamando system da biblioteca os - comando ping
#-n -ping de pacotes que serão 6 {}
os.system('ping -n 6 {}'.format(ip_ou_host))
print('#' * 60)

