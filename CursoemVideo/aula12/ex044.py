"""
Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e a condição de 
pagamento: 
- a vista dinheiro/pix: 10% de desconto
- a vista no cartao: 5% de desconto
- em ate 2x no cartao: preço normal
- 3x ou mais no cartao: 20% de juros 
""" 
precoInicial = float(input("Digite o valor inicial do produto: "))
pagamento = int(input("Digite a forma de pagamento:\n1 - dinheiro/pix\n2 - Cartao a vista\n3 - 2x no cartao\n4 - a partir de 3x no cartao\n"))

if pagamento == 1:
    newPreco = precoInicial * 0.9
    print("Preço com desconto - 10%\nPreço a receber: R${}.".format(newPreco))
elif pagamento == 2:
    newPreco = precoInicial * 0.95
    print("Preço com desconto - 5%\nPreço a receber: R${}.".format(newPreco))
if pagamento == 3:
    print("Preço sem desconto\nPreço a receber: R${}.".format(precoInicial))
if pagamento == 4:
    newPreco = precoInicial * 1.2
    print("Preço com juros - 20%\nPreço a receber: R${}.".format(newPreco))
