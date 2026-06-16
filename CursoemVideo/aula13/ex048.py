"""
Faca um programa que calcule a soma entre todos os numeros impares que sao multiplos de tres e que se encontram no intervalo
de 1 até 500.
"""
s = 0
for i in range(1, 500):
    if i % 3 == 0 and i % 2 == 1: 
        s += i
print("A soma de todos os numeros impares e multiplos de 3, no intervalo de 1 a 500 é {}.".format(s))
