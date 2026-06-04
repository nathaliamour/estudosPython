#Crie um programa que leia duas notas de um aluno e calcule sua media. 
#mostre uma mensagem no final, de acordo com a media. abaixo de 5.0 - reprovado
#entre 5 e 6.9 - recuperaçao e igual ou superior a 7 - aprovado
print("--Cálculo de média--")
n1 = float(input("Digite a primeira nota do aluno: "))
n2 = float(input("Digite a segunda nota do aluno: "))

media = (n1 + n2)/2

if media < 5: 
    print("A média do aluno foi {}.\nStatus do aluno: Reprovado!".format(media))
elif media >= 5 and media < 6.9: 
    print("A média do aluno foi {}.\nStatus do aluno: Recuperação!".format(media))
else: 
    print("A média do aluno foi {}.\nStatus do aluno: Aprovado!".format(media))
