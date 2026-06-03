#Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80 km/h, calcule a multa
#R$ 7,00 por km que exceder os 80 km/h

velLimite = int(input("Digite a velocidade máxima permitida em km/h: "))
vel = int(input("Digite o valor da velocidade do veículo, em km/h: "))

if vel > velLimite: 
    multa = (vel - velLimite) * 7
    print("Você foi multado!\nO valor da multa será R${}.".format(multa))
else: 
    print("Fique tranquilo!\nVocê não foi multado!")
    