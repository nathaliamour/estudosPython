"""
Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando os espacos.
Ex: apos a sopa; a sacada da casa; a torre da derrota; o lobo ama o bolo; anotaram a data da maratona.
"""
print("-- Palíndromos --")
frase = input("Digite a frase a ser verificada: ").upper()
frase = frase.replace(" ", "")
inverso = frase[::-1]

verifica = 0
for i in range(0, len(frase)):
    if frase[i] == inverso[i]: 
        verifica += 1

if verifica == len(inverso):
    print("A frase é um palíndromo!")   
    print(inverso)
else:
    print("A frase não é um palíndromo!")
    print(inverso)   
