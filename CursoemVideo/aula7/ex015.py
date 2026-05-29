#Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade
#de dias pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.
rodados = float(input('Escreva a quantidade de Km percorridos com o carro alugado: '))
dias = int(input('Escreva a quantidade de dias que você ficou com o carro: '))
preco = (60 * dias) + (0.15 * rodados)

print('Você esteve com o carro por {} dias e percorreu {} Km. \nO valor total do aluguel é R$ {:.2f}'.format(dias, rodados, preco))
