"""
Faça um programa que leia um número qualquer e mostre o seu fatorial.
"""
print("--Vamos calcular fatorial--")
num = int(input("Digite o número: "))
ciclo = num
fatorial = 1
print("{}! = ".format(num), end = "")
while ciclo != 0:
    fatorial *= ciclo
    print("{}".format(ciclo), end="")
    print(" x " if ciclo > 1 else " = ", end = "")
    ciclo -= 1
print(fatorial)
