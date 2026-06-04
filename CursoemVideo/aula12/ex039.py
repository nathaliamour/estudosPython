#Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo
#com sua idade: 
#Se ele ainda vai se alistar ao serviço militar
#Se é a hora de se alestar
#Se já passou do tempo de alistamento. 
#Seu programa também deverá mostrar o tempo que falta ou que passou do prazo
print("--Verificação de necessidade de alistamento--")
ano = int(input("Digite o ano de nascimento do jovem: "))
idade = 2026 - ano

if idade < 18: 
    print("O jovem possui {} anos.\nAinda irá se alistar ao serviço militar!".format(idade))
elif idade == 18: 
    print("O jovem possui {} anos.\nEstá na hora de se alistar!".format(idade))
else:
    print("O jovem possui {} anos.\nJá passou do tempo de alistamento!".format(idade))
