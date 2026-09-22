"""
Faça um programa que mostre a tabuada de vários números, um de cada vez, 
para cada valor digitado pelo usuário. O programa será interrompido quando o número 
solicitado for negativo.
"""
while True:
    numero = int(input("Digite um número para ver sua tabuada [negativo para parar]: "))

    if numero < 0:
        break

    print(f"\nTabuada do {numero}:")

    for multiplicador in range(1, 11):
        resultado = numero * multiplicador
        print(f"{numero} x {multiplicador} = {resultado}")

print("Programa encerrado.")