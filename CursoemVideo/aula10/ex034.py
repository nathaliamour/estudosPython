#Escreva um programa que pergunte o salario de um funcionario e calcule o valor do seu aumento. 
#Para salarios superiores a R$1.250,00, calcule um aumento de 10%. 
#Para inferiores ou iguais, o aumento é de 15%. 
salario = float(input("Digite o valor do salário do funcionário: "))

if salario > 1250: 
    newSalario = salario * 1.1
    print("O novo salário terá um aumento de 10%, totalizando R${}.".format(newSalario))
else: 
        newSalario = salario * 1.15
        print("O novo salário terá um aumento de 15%, totalizando R${}.".format(newSalario))
