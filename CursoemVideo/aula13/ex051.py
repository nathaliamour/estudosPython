"""
Desenvolva um programa que leia o primeiro termo e a razao de uma PA. No final, mostre os 10 primeiros termos dessa 
progressao. 
"""
print("Brincando com Progressao Aritmética")
n = int(input("Digite o primeiro termo da P.A.: "))
r = int(input("Digite a razao dessa P.A.: "))
print("Os primeiros 10 termos dessa P.A. são: ")
for i in range(0, 10): 
    print(n)
    n += r
    
