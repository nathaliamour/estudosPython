#Faca um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triangulo retangulo, calcule e mostre o comprimento da hipotenusa.
from math import sqrt
co = float(input('Digite o valor do cateto oposto: '))
ca = float(input('Digite o valor do cateto adjacente: '))
hi = sqrt(pow(co,2)+pow(ca,2))

print('O triângulo retângulo cujo catetos valem {} e {}, possui hipotenusa valendo {}.'.format(co,ca,hi))

#hipo = math.hypot(co, ca)   --- muito mais simples

