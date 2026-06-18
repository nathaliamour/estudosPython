#Manipulando Cadeias de textos
# frase = 'Curso em vídeo Python'  --  Cadeia de caracteres ou string
#Fatiamento - frase[9] -- somente o caracter que leva o indice 9
#frase[9:13] - ele pega do caracter de indice 9 até o caracter de indice 12 (o 13 nao entra, o range é só até o anterior do ultimo numero
#frase[9:21:2] - pega do 9 ao 20, mas pulando de 2 em 2
#frase[:5] - pega do 0 até o caracter de numero 4
#frase[15:] - pega do caracter 15 até o ultimo
#frase[9::3] - pega do 9 e vai até o final, mas pulando de 3 em 3
#frase[::-1] - inverte a string

#análise de string
#len(frase) - quantidade de caracteres da frase
#frase.count('o') - conta quantas vezes existe a letra o
#frase.count('o',0,13) - conta os 'o' do indice 0 ao 12
#frase.find('deo') - diz quantas vezes ele encontra deo e diz onde ele encontra o inicio desse trecho (o indice)
#frase.find('Android') - uma strg que nao existe na frase, ele retorna -1
#frase.rfind('palavra') - procura a partir do lado direito
#'Curso' in frase - operador in diz se existe ou nao essa str retornando True ou False

#Transformacao
#frase.replace('Python',"Android')
#frase.upper() - deixar tudo maiusculo
#frase.lower()
#frase.capitalize() - só a primeira letra maiuscula
#frase.title() - capitalize palavra por palavra
#frase.strip() - remove todos os espacos do final e do inicio de uma strg
#frase.rstrip() - remove somente o ultimo espaco
#frase.lstrip() - remove somente o inicio (esquerda)
#lista.sort()

#divisao
#frase.split() - divide cada palavra em outras listas

#juncao
#'-'.join(frase) - junta as palavras utilizando um - para separá-las

frase = 'Curso em Vídeo Python'
