#Desenvolva um programa que pergunte a distancia de uma viagem em KM. Calcule o preco da passagem,
#cobrando R$0,50 por KM para viagens de até 200KM e R$0,45 para viagens mais longas.

distance = float(input("Digite a distância da viagem: "))
print("Calculando o valor da passagem...")

if distance <= 200:
    passagem = distance * 0.5
    print("Sua passagem custará R${}.".format(passagem))
else: 
    passagem = distance * 0.45
    print("Sua passagem custará R${}.".format(passagem))
