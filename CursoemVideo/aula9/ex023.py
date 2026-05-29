#Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados.
num = input('Digite um número de 0 a 9999: ')
numConc = '0000' + num
numI = numConc[::-1]

print('Unidade: {}.\nDezena: {}.\nCentena: {}.\nMilhar: {}'.format(numI[0], numI[1], numI[2], numI[3]))