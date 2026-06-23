c = 1 
while c != 10: 
    print(c)
    c+=1
print("Acabou!")

r = 'S'
while r == 'S':
    n = int(input("Digite um valor: "))
    r = str(input("Quer continuar? [S/N] ")).upper()
print("Fim!")

i = 1
par = impar = 0
while n!= 0:
    i = int(input("Digite um valor: "))
    if i % 2 == 0: 
        par += 1
    else: 
        impar += 1
print("Você digitou {} números pares e {} números ímpares!".format(par, impar))
