"""
Faca um programa que leia o peso de cinco pessoas. No final, mostre qual foi o maior e o menor peso lidos.
"""
peso = []
for i in range(0, 5):
    peso.append(float(input("Digite o peso de uma pessoa de cada vez: ")))
peso.sort()
print("O maior peso registrado foi {} Kg.".format(peso[4]))
print("O menor peso registrado foi {} Kg.".format(peso[0]))
