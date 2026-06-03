#Desenvolva um programa que leia o comprimento de tres retas e diga ao usuario se eles podem ou nao
#formar um triangulo.
print("Vamos trabalhar com triângulos...\nEscolha 3 retas e veremos se elas formam um triângulo!")
l1 = float(input("Escreva o tamanho da primeira reta: "))
l2 = float(input("Escreva o tamanho da segunda reta: "))
l3 = float(input("Escreva o tamanho da terceira reta: "))

if (l1 + l2) > l3 and (l1 + l3) > l2 and (l2 + l3) > l1:
    print("Uau! As retas {}, {} e {} formam um triângulo!".format(l1, l2, l3))
else: 
    print("As retas {}, {} e {} não podem formar um triângulo!".format(l1, l2, l3))
