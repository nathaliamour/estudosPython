#Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada.
import math

n = int(input('Digite um número inteiro:'))
dobro = n*2
triplo = n*3
raiz = math.sqrt(n)    #n**(1/2)


print('O número escolhido foi {}, seu dobro é {}, seu triplo é {} e sua raiz quadrada é {:.2f}.'.format(n, dobro, triplo, raiz))
#print('O número escolhido foi {}, seu dobro é {}, seu triplo é {} e sua raiz quadrada é {:.2f}.'.format(n, (n*2), (n*3), (n**(1/2)))
