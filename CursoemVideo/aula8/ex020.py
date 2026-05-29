#O mesmo professor do desafio anterior quer sortear a ordem de apresentação de trabalhos dos alunos.
# Faca um programa que leia o nome dos quatro alunos e mostre
#a ordem sorteada
import random
aluno1 = input('Digite o nome do primeiro aluno: ')
aluno2 = input('Digite o nome do segundo aluno: ')
aluno3 = input('Digite o nome do terceiro aluno: ')
aluno4 = input('Digite o nome do quarto aluno: ')

escolhido = [aluno1, aluno2, aluno3, aluno4]

print('A ordem de apresentação é: {}.'.format(random.sample(escolhido, k=4)))

#random.shuffle(escolhido) / print(lista)  --outro jeito de fazer