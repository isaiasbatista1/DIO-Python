import hashlib

arquivo1 = 'a.txt'
arquivo2 = 'b.txt'

hash1 = hashlib.new('ripemd160')
hash1.update(open(arquivo1, 'rb').read()) # rb é o método de abertura para leitura no modo binário

hash2 = hashlib.new('ripemd160')

hash2.update(open(arquivo2, 'rb').read())

# digest = resume os dados passados para o método update
if hash1.digest() != hash2.digest():
    print(f'O arquivo: {arquivo1} é diferente do arquivo: {arquivo2}')
    print("O hash do arquivo a.txt é: ", hash1.hexdigest())  # mostrando o hash do arquivo a.txt
    print("O hash do arquivo b.txt é:", hash2.hexdigest())  # mostrando o hash do arquivo b.txt

else:
    print(f'O arquivo: {arquivo1} é igual ao arquivo: {arquivo2}')
    print("O hash do arquivo a.txt é: ", hash1.hexdigest())  # mostrando o hash do arquivo a.txt
    print("O hash do arquivo b.txt é:", hash2.hexdigest())  # mostrando o hash do arquivo b.txt
