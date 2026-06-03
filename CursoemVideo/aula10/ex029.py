#Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80 km/h, 
#mostre uma mensagem dizendo que ele foi multado. A multa vai custar R$7,00 por cada KM acima do limite.
vel = int(input("Digite o valor da velocidade do veículo, em km/h: "))

if vel > 80: 
    multa = (vel - 80) * 7
    print("Você foi multado!\nO valor da multa será de R${}.".format(multa))
else: 
    print("Fique tranquilo!\nVocê não foi multado!")
