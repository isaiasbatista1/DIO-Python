'''
webbrowser - fornece uma interface de alto nível para permitir a exibição de documentos Web aos usuários.

tkinter - fornece interface padrão do Python para o kit de ferramentas gráficas TK
'''

import webbrowser

from tkinter import *

root = Tk( )

root.title('Abrir Browser') #título
root.geometry('300x200')    #dimensões

#essa função vai fazer abrir o site do google
def google():
    webbrowser.open('www.google.com')

mygoogle = Button(root, text="Abrir o google", command=google).pack(pady=20)
root.mainloop()
