"""
Crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre quantas pessoas ainda nao atingiram 
maioridade e quantos já sao maiores.
"""
maior = []
lista = []
print("-- Data de Nascimento --")
for i in range(0, 7):
    ano = int(input("Digite o ano de nascimento da pessoa: "))
    lista.append(ano)
for i in range(0, 7):
    ehMaior = 2026 - lista[i]
    if ehMaior >= 18: 
        maior.append(ehMaior)
print("\nDentre as pessoas apresentadas, {} são maior de idade e {} são menores de idade.".format(len(maior), 7 - len(maior)))
