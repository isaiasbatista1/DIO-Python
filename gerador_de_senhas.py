import random, string

#Uma boa prática de segurança da informação é ter uma senha de pelo menos 16 caracteres.
tamanho = int(input("Digite o tamanho de senha que você deseja:"))

#ascii_letters diz respeito a letras maiúsculas e minúsculas
chars = string.ascii_letters + string.digits + '_*!@#$(/:.,)-=+'

#os.random gera números aleatóreos com base no sistema operacional
rnd = random.SystemRandom()

print(''.join(rnd.choice(chars) for i in range(tamanho)))
