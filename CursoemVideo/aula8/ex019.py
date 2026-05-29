#Um professor quer sortear um dos seus quatro alunos para apagar o quadro. Faca um programa que ajude ele, lendo o nome deles e escrevendo o nome escolhido.
import random
aluno1 = input('Digite o nome do primeiro aluno: ')
aluno2 = input('Digite o nome do segundo aluno: ')
aluno3 = input('Digite o nome do terceiro aluno: ')
aluno4 = input('Digite o nome do quarto aluno: ')

escolhido = [aluno1, aluno2, aluno3, aluno4]

print('O aluno escolhido foi: {}.'.format(random.choice(escolhido)))

