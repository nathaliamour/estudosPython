#Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros
metro = float(input('Digite o valor a ser convertido em metros: '))
cent = metro * 100
mili = metro * 1000

print('O valor, em centímetros, é {}. Já em milímetros é {}.'.format(cent, mili))
