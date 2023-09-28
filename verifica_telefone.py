#Biblioteca phonenumbers - informações básicas de um número de telefone, validação de um número de telefone.

import phonenumbers
from phonenumbers import geocoder

phone = input("Digite o telefone no formato: +551140028922: ") #informar o número mestre(do país, operadora e o número em seguida.)

phone_numbers = phonenumbers.parse(phone)

print(geocoder.description_for_number(phone_numbers, 'pt'))
