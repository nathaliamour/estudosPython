"""
Refaça o DESAFIO 035 dos triangulos, acrescentando o recurso de mostrar que tipo de triangulo será formado: 
- equilatero: todos os lados iguais
- isósceles: dois lados iguais
- escaleno: todos os lados diferentes
"""
print("Vamos trabalhar com triângulos...\nEscolha 3 retas e veremos se elas formam um triângulo!")
l1 = float(input("Escreva o tamanho da primeira reta: "))
l2 = float(input("Escreva o tamanho da segunda reta: "))
l3 = float(input("Escreva o tamanho da terceira reta: "))

if (l1 + l2) > l3 and (l1 + l3) > l2 and (l2 + l3) > l1:
    print("Uau! As retas {}, {} e {} formam um triângulo!".format(l1, l2, l3))
    if l1 == l2 and l2 == l3: 
        print("Se trata de um triângulo equilátero!\n")
    elif l1 == l2 or l2 == l3: 
        print("Se trata de um triângulo isósceles!\n")
    elif l1 != l2 and l2 != l3: 
        print("Se trata de um triângulo escaleno!\n")
else: 
    print("As retas {}, {} e {} não podem formar um triângulo!\n".format(l1, l2, l3))
