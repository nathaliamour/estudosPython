"""
Crie um programa que leia vários números inteiros pelo teclado. O programa só vai 
parar quando o usuário digitar o valor 999, que é a condição de parada. No final, 
mostre quantos números foram digitados e qual foi a soma entre eles (desconsiderando 
o flag).
"""
n = int(input("Digite a quantidade de elementos: "))

a = 0
b = 1

for i in range(n):
    print(a, end=" ")
    a, b = b, a + b