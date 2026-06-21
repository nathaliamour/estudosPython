"""
Desenvolva um programa que leia o nome, idade e sexo de quatro pessoas. No final do programa, mostre:
1. A média de idade do grupo
2. Qual é o nome do homem mais velho
3. Quantas mulheres tem menos de 20 anos.
"""
dados = []
lista_idade = []
for i in range(1, 5):
    pessoa = []
    print("Dados da {}a pessoa".format(i))
    nome = input("Digite o nome da {}a pessoa: ".format(i))
    nome.strip()
    nome.title()
    idade = int(input("Digite a idade da {}a pessoa: ".format(i)))
    lista_idade.append(idade)
    sexo = input("Digite 'F' para sexo feminino e 'M' para sexo masculino: ").upper()
    sexo.strip()
    pessoa.extend([nome, idade, sexo])
    print(pessoa)
    dados.append(pessoa)
print(dados)
maior_idade = max(lista_idade)
posicao_maior_idade = lista_idade.index(max(lista_idade))
soma = (dados[0][1]) + (dados[1][1]) + (dados[2][1]) + (dados[3][1])
media = soma/4
print("A média da idade das pessoas desse grupo é {} anos.".format(media))
print("" \
"")