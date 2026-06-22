"""
Desenvolva um programa que leia o nome, idade e sexo de quatro pessoas. No final do programa, mostre:
1. A média de idade do grupo
2. Qual é o nome do homem mais velho
3. Quantas mulheres tem menos de 20 anos.
"""
dados = []
for i in range(1, 5):
    pessoa = []
    print("Dados da {}a pessoa".format(i))
    nome = input("Digite o nome da {}a pessoa: ".format(i)).strip().title()
    idade = int(input("Digite a idade da {}a pessoa: ".format(i)))
    sexo = input("Digite 'F' para sexo feminino e 'M' para sexo masculino: ").upper().strip()
    pessoa.extend([nome, idade, sexo])
    dados.append(pessoa)
print(dados)
soma = (dados[0][1]) + (dados[1][1]) + (dados[2][1]) + (dados[3][1])
media = soma/4
print("A média da idade das pessoas desse grupo é {} anos.".format(media))
idade_homens = []
posicao_idade_homens = []
idade_mulheres = []
posicao_idade_mulheres = []
for c in range (0, 4): 
    if dados[c][2] == 'M':
        idade_homens.append(dados[c][1])
        posicao_idade_homens.append(c)
    else: 
        idade_mulheres.append(dados[c][1])
        posicao_idade_mulheres.append(c)        
if idade_homens:
    maior_idade = max(idade_homens)
    posicao_maior_idade = posicao_idade_homens[idade_homens.index(max(idade_homens))]
    print("O homem mais velho do grupo é o {}.".format(dados[posicao_maior_idade][0]))
else: 
    print("Nao há homens no grupo!")
count = 0
for n in range(0, len(idade_mulheres)):    #for idade in idade_mulheres:
    if idade_mulheres[n] <= 20: 
        count += 1
print("Esse grupo possui {} mulheres com 20 anos ou menos.".format(count))
