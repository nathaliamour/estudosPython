#Crie um programa que leia uma frase pelo teclado e mostre: 1. Quantas vezes aparece a letra "a". 
#2. Em que posiçao ela aparece a primeira vez. 3. Em que posiçao ela aprece a última vez.
frase = input("Digite uma frase: ").strip()
frase = frase.upper()
print("A letra 'a' aparece {} vezes.\nAparece pela primeira vez na posição {}.\nAparece pela " \
"última vez na posição {}.".format(frase.count('A'), frase.find('A')+1, frase.rfind('A')+1))
