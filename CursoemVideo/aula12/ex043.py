"""
Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu IMC e mostre seu status, 
de acordo com a tabela abaixo: 
- Abaixo de 18.5: Abaixo do peso
- Entre 18.5 e 25: Peso ideal
- 25 até 30: Sobrepeso
- 30 a 40: Obesidade
- Acima de 40: Obesidade Mórbida
"""
peso = float(input("Digite o seu peso, em kg: "))
altura = float(input("Digite a sua altura, em metros: "))
imc = peso / (altura * altura)

print("O seu IMC tem valor {}.".format(imc))

if imc < 18.5:
    print("Voce está abaixo do peso!")
elif imc >= 18.5 and imc < 25: 
    print("Voce está no seu peso ideal!")
elif imc >= 25 and imc < 30: 
    print("Voce está com sobrepeso!")
elif imc >= 30 and imc < 40: 
    print("Voce está com obesidade!")
else: 
    print("Voce está com obesidade mórbida!")
