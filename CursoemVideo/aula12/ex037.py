#Escreva um programa que \leia um numero inteiro qualquer e peça para o usuario escolher
#qual será a base de conversao: 
# 1 para binário
# 2 para octal 
# 3 para hexadecimal
print("--Converção de números decimais--")
num = int(input("Escreva um número inteiro qualquer: "))
base = int(input("Escolha a base para a qual iremos converter:\n1 - binário" \
"\n2 - octal\n3 - hexadecimal\nConsidere uma das opções acima: "))

if base == 1: 
    newNum = bin(num)
    print("Você escolheu o número {}.\nConvertendo...\n{} em binário é {}!".format(num, num, newNum))
elif base == 2: 
    newNum = oct(num)
    print("Você escolheu o número {}.\nConvertendo...\n{} em octal é {}!".format(num, num, newNum))
elif base == 3: 
    newNum = hex(num)
    print("Você escolheu o número {}.\nConvertendo...\n{} em hexadecimal é {}!".format(num, num, newNum))
else: 
    print("Escolha uma opção válida!")