"""
Refaca o desafio 009, mostrando a tabuada de um numero que o usuario escolher, só que agora utilizando um laco for.
""" 
n = int(input('Digite um número inteiro: '))

print('-' * 16)
print('--Tabuada do {}--'.format(n))
for i in range(1, 11): 
    print('{} x {:2} = {}'.format(n, i, n * (i)))
print('-' * 16)
