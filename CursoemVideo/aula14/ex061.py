"""
Refaça o desafio 051, lendo o primeiro termo e a razao de uma PA, 
mostrando os 10 primeiros termos da progressao usando estrutura while.
"""
print("Brincando com Progressao Aritmética")
n = int(input("Digite o primeiro termo da P.A.: "))
r = int(input("Digite a razao dessa P.A.: "))
c = 10
print("Primeiro termo: {}\nRazão: {}\nP.A: ".format(n, r), end = "")
while c != 0: 
    print("{}".format(n), end = "")
    print(", " if c > 1 else ".", end = "")
    n += r
    c -= 1
