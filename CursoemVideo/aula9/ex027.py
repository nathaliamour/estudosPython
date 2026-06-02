#Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o 
#último nome separadamente.
nome = input("Digite o seu nome completo: ").strip()
nome = nome.split()
FirstName = nome[0]
nome = nome[::-1]
LastName = nome[0]
print("O seu primeiro nome é {}, e o seu último sobrenome é {}.".format(FirstName,LastName))
