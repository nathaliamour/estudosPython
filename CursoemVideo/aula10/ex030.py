#Crie um programa que leia um numero inteiro e mostra na tela se ele é par ou impar. 
num = int(input("Digite um número inteiro para verificação: "))

resto = num % 2

if resto == 1: 
    print("O número {} é ímpar!".format(num))
else: 
    print("O número {} é par!".format(num))
