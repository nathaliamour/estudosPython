"""
Faca um programa que leia um numero inteiro e diga se ele é ou nao um numero primo.
"""

print("-- É um número primo? --")
n = int(input("Digite um número: "))
for i in range(2, int(n ** 0.5) + 1):
    if n % i != 0: 
        print("O número {} é primo!".format(n))
    else: 
        print("O número {} não é primo!".format(n))
