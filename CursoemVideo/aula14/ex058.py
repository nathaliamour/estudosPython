"""
Melhore o jogo do Desafio 028 onde o computador vai "pensar" em um número de 0 a 10. Só que agora o jogador vai tentar adivinhar
até acertar, mostrando no final quantos palpites foram necessários para vencer.
"""
import random 
num = random.randint(0, 10)
palpite = int(input("Vou escolher um número entre 0 e 10...\nConsegue adivinhar o número escolhido?\nDigite o seu palpite: "))
count = 1
while num != palpite:
    count += 1 
    if num == palpite:
        print("Uau! Você venceu!")
    else: 
        print("Não foi dessa vez!\nrs\nrs\nrs\nTente novamente!")
        palpite = int(input("Digite o seu palpite: "))
print("Você conseguiu! O número era {} e você precisou de {} palpites para vencer!".format(num, count))
