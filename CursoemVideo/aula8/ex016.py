#Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela a sua porção inteira.
#primeira maneira
import math
num = float(input('Digite um valor:'))
parteInt = int(num)
print('O número digitado foi {} e a sua parte inteira é {}'.format(num, parteInt))
print('-'*12)
print('O número digitado foi {} e a sua parte inteira é {}'.format(num, math.trunc(num)))

