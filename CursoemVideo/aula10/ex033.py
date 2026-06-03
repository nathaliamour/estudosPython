#Faca um programa que leia tres numeros e mostre qual é o maior e qual é o menor
n1 = float(input("Digite o primeiro número a ser analisado: "))
n2 = float(input("Digite o segundo número a ser analisado: "))
n3 = float(input("Digite o terceiro número a ser analisado: "))

if n1 < n2 and n1 < n3: 
    if n2 < n3: 
        print("O menor número é {} e o maior é {}".format(n1, n3))
    else: 
        print("O menor número é {} e o maior é {}".format(n1, n2))
elif n2 < n1 and n2 < n3: 
    if n1 < n3: 
        print("O menor número é {} e o maior é {}".format(n2, n3))
    else: 
        print("O menor número é {} e o maior é {}".format(n2, n1))
else: 
    if n2 < n1: 
        print("O menor número é {} e o maior é {}".format(n3, n1))
    else:
        print("O menor número é {} e o maior é {}".format(n3, n2))
