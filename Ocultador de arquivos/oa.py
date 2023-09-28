import ctypes
#Essa biblioteca fornece tipos de dados compatíveis com C e permite funções de chamada em DLLs ou bibliotecas compartilhadas.

atributo_ocultar = 0x02 #esse é o arquivo em hexadecimal que será ocultado

#dentro do kernel32 será setado e reescrito o arquivo ocultar.txt
retorno = ctypes.windll.kernel32.SetFileAttributesW('ocultar.txt', atributo_ocultar)

if retorno:
    print("Arquivo foi ocultado")
else:
    print("O Arquivo não foi ocultado")


