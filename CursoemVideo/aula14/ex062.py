"""
Melhore o Desafio 061, perguntando para o usuário se ele quer mostrar mais alguns termos. 
O programa encerra quando ele disser que quer mostrar 0 termos. 
"""
print("Brincando com Progressao Aritmética")
n = int(input("Digite o primeiro termo da P.A.: "))
r = int(input("Digite a razao dessa P.A.: "))
c = 10
print("Primeiro termo: {}\nRazão: {}\nP.A: ".format(n, r), end = "")
i = 1
while i != 0: 
    while c != 0: 
        print("{}".format(n), end = "")
        print(", " if c > 1 else ".", end = "")
        n += r
        c -= 1
    i = int(input("\nVocê desejar mostrar mais alguns termos? [1/0]"))
