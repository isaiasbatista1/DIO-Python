from urllib.request import urlopen
import requests
from bs4 import BeautifulSoup

#Site que serão coletadas as informações
url = "http://www.pudim.com.br/"

#Obtendo os dados do site
html = requests.get(url).content

#Formatando os dados
dados = BeautifulSoup(html, 'html.parser')
print(dados.prettify())

#formatando a div que armazena o email
email = dados.find('div', class_="email")
print(email)

#fazendo uma coleta melhor usando o prettify
print(email.prettify())

#buscando a class email
email = dados.find('div', class_='email')

#coletando a tag dentro da div email
link = email.find("a")
print("1", link)

#pegando o texto somente
print("2", link.text)

#coletando o endereço do link
print("3", link.attrs['href'])