#Escreva um programa que faca o computador "pensar" em um numero inteiro entre 0 e 5 e 
#peca para o usuario tentar descobrir qual foi o numero escolhido pelo computador. O programa devera
#escrever na tela se o usuario venceu ou perdeu.
import random 

num = random.randint(1,5)

palpite = int(input("Vou escolher um número entre 1 e 5...\nConsegue adivinhar o número escolhido?\nDigite o seu palpite: "))

if num == palpite:
    print("Uau! Você venceu!")
else: 
    print("Não foi dessa vez!\nrs\nrs\nrs\nO número escolhido foi {}".format(num))
    