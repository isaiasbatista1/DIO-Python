import itertools

string = input("String a ser permutada: ")

resultado = itertools.permutations(string, len(string))

for i in resultado: #vai gerar um caractere aleatóreo e juntar com outro
    print(''.join(i))




