#Crie um programa que leia o nome de uma pessoa e diga se ela tem "Silva" no nome.
nome = input('Digite o seu nome completo: ').strip()
nome = nome.upper()
print("Seu nome tem 'Silva'? {}".format(nome.find('SILVA')>-1))