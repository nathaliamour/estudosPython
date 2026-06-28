"""
Faça um programa que leia o sexo de uma pessoa, 
mas só aceite valores 'M' ou 'F'. Caso esteja 
errado, peça a digitação novamente até ter um valor correto.
"""
nome = input("Digite o nome da pessoa: ").upper().strip()
genero = str(input("Digite o gênero da pessoa: [F/M]")).upper().strip()

while genero not in 'MmFf':
    genero = str(input("Gênero inválido. Digite novamente, por favor!\nDigite o sexo da pessoa: [F/M]")).upper().strip()
print("Gênero {} registrado com sucesso!".format(genero))
