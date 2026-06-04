#Escreva um programa para aprovar o empréstimo bancário para a compra
#de uma casa. O programa vai perguntar o valor da casa, 
#o salário do comprador e em quantos anos ele vai pagar. 
#Calcule o valor da prestaçao mensal, sabendo que ela nao pode exceder
#30% do salário ou entao o emprestimo será negado. 
print("--Programa de Verificação de Crédito--")
valor = float(input("Qual o valor da casa? "))
salario = float(input("Qual o salário do comprador? "))
tempo = float(input("Por quanto tempo, em anos, será realizado o pagamento? "))
tempoMeses = tempo * 12
taxa = float(input("Digite a taxa de juros mensal: \n(lembre-se de colocar em decimal - ex.:0.8% = 0.008)"))

prestacao = valor * ((taxa*((1+taxa)**tempoMeses))/(((1+taxa)**tempoMeses)-1))
prestacaoMax = salario * 0.3
                     
if prestacao <= prestacaoMax: 
    print("Empréstimo aprovado!\nO valor da prestação mensal será {:.2f}.".format(prestacao))
else: 
    print("Empréstimo negado!\nO valor mínimo calculado para a prestação, R${:.2f}, " \
    "excede o valor máximo permitido para o comprador.".format(prestacao))
