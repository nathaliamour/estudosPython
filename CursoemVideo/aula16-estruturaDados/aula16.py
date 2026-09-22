lanche = ("Hamburguer", "Suco", "Pizza", "Pudim")
print(lanche[1])  # Suco
print(lanche[-2])  # Pizza          
print(lanche[2:])
print (len(lanche))  # 4

for comida in lanche:
    print(f"Eu vou comer {comida}") 

for cont in range(0, len(lanche)):
    print(f"Eu vou comer {lanche[cont]} na posição {cont}")

for pos, comida in enumerate(lanche):
    print(f"Eu vou comer {comida} na posição {pos}")

print(sorted(lanche))  # Ordena a tupla

a = (2, 5, 4)
b = (5, 8, 1, 2)        
c = b + a  # Concatena as tuplas
print(c) 

print(c.count(5))  # Conta quantas vezes o valor 5 aparece na tupla
print(c.index(8))  # Mostra a posição do valor 8 na tupla

pessoa = ("Gustavo", 39, "M", 99.88)
print(pessoa)  # Mostra a tupla completa