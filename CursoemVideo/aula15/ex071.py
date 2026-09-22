"""
Crie um programa que simule o funcionamento de um caixa eletrônico. No início, pergunte 
ao usuário qual será o valor a ser sacado (número inteiro) e o programa vai informar 
quantas cédulas de cada valor serão entregues.
OBS: Considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1.
"""
valor = int(input("Qual valor você deseja sacar? R$ "))

restante = valor
cedula = 50

while restante > 0:
    quantidade = restante // cedula
    restante = restante % cedula

    if quantidade > 0:
        print(f"{quantidade} cédula(s) de R${cedula}")

    if cedula == 50:
        cedula = 20
    elif cedula == 20:
        cedula = 10
    elif cedula == 10:
        cedula = 1

print("Saque finalizado.")