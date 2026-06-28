"""
Crie um programa que leia dois valores e mostre um menu na tela: 
[1] somar
[2] multiplicar
[3] maior
[4] novos números
[5] sair do programa

Seu programa deverá realizar a operação solicitada em cada caso.
"""
num1 = int(input("Digite o primeiro valor: "))
num2 = int(input("Digite o segundo valor: "))
operacao = 0
while operacao != 5:
    operacao = int(input("\n[1] somar\n[2] multiplicar\n[3] maior\n[4] novos números\n[5] sair do programa\n" \
    "Digite qual operação você deseja realizar entre os números:"))
    if operacao == 1: 
        resultado = num1 + num2
        print("\nSoma: {} + {} = {}".format(num1, num2, resultado))
    elif operacao == 2: 
        resultado = num1 * num2
        print("\nMultiplicação: {} x {} = {}".format(num1, num2, resultado))
    elif operacao == 3: 
        if num1 > num2:
            print("\nO número {} é maior que o número {}.".format(num1, num2))
        elif num1 == num2: 
            print("\nOs números são iguais!")
        else: 
            print("\nO número {} é maior que o número {}.".format(num2, num1))
    elif operacao == 4: 
        num1 = int(input("\nDigite o primeiro valor: "))
        num2 = int(input("Digite o segundo valor: "))
print("\nO programa foi encerrado!")
