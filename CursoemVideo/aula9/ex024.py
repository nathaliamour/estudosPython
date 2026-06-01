#Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com o nome "SANTO".
city = (str(input('Digite o nome de uma cidade: '))).upper() 
print("Verificando se começa com 'SANTO'...'")
verifica = city.find('SANTO')
print(verifica)

