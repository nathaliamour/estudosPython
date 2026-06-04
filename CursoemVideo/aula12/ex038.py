#Escreva um programa que leia dois numeros inteiros e compare-os, 
#mostrando na tela uma mensagem: 
# O primeiro valor é maior 
# O segundo valor é maior 
# Nao existe valor maior, os dois sao iguais
print("--Maior ou Menor--")
n1 = int(input("Digite o primeiro número: "))
n2 = int(input("Digite o segundo número: "))

if n1 > n2: 
    print("Você escolheu {} e {}. \nO primeiro valor é maior!".format(n1, n2))
elif n2 > n1: 
    print("Você escolheu {} e {}. \nO segundo valor é maior!".format(n1, n2))
else: 
    print("Não existe valor maior, os dois são iguais.")
    