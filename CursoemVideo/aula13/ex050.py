"""
Desenvolva um programa que leia seis numeros inteiros e mostre a soma apenas daqueles que forem pares. Se o valor 
digitado for impar, desconsidere-o.
"""
print("--- Somando números pares ---")
s = 0
for i in range(0, 6):
    n = int(input("Digite um número: "))
    if n % 2 == 0: 
        s += n
print("A soma dos números pares digitados é {}".format(s))
