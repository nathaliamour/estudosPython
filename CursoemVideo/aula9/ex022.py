#Crie um programa que leia o nome completo de uma pessoa e mostre: O nome com todas as letras maiúsculas e minúsculas.
#Quantas letras tem o nome (ser considerar os espaços) Quantas letras tem o primeiro nome.
nome = str(input('Digite o seu nome completo: ')).strip()
print('Seu nome completo, maiúsculo, é: {}\nSeu nome completo, minúsculo, é: {} '.format(nome.upper(), nome.lower()))
nomeNospace = nome.split()
primeiroNome = nomeNospace[0]
nomeNospace = ''.join(nomeNospace)
print('Seu nome completo possui {} letras.'.format(len(nomeNospace)))
print('Seu primeiro nome é {} e possui {} letras. '.format(primeiroNome,len(primeiroNome)))

