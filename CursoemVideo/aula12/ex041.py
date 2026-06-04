"""
a confederaçao nacional de nataçao precisa de um programa que leia o ano de nascimento de um atleta e mostre sua categoria, de acordo com a 
#idade. 
#Ate 9 anos - mirim
Até 14 anos - infantil 
Até 19 anos - Junior 
Até 20 anos - Senior 
Acima - Master
"""
print("--Categoria - Atletismo--")
ano = int(input("Digite o ano de nascimento do atleta: "))
idade = 2026 - ano
if idade <= 9:
    print("O atleta tem {} anos.\nCategoria: Mirim.".format(idade))
elif idade <= 14:
    print("O atleta tem {} anos.\nCategoria: Infantil.".format(idade))
elif idade <= 19:
    print("O atleta tem {} anos.\nCategoria: Junior.".format(idade))
elif idade <= 20: 
    print("O atleta tem {} anos.\nCategoria: Sênior".format(idade))
else: 
    print("O atleta tem {} anos.\nCategoria: Master".format(idade))


