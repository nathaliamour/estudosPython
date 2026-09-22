"""
Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato Brasileiro
de Futebol, na ordem de colocação. Depois mostre:
a) Apenas os 5 primeiros colocados.
b) Os últimos 4 colocados da tabela.
c) Uma lista com os times em ordem alfabética.
d) Em que posição na tabela está o time da Chapecoense.
"""
times = ('Corinthians', 'Palmeiras', 'Santos', 'Grêmio', 'Cruzeiro', 'Flamengo', 'Vasco', 
         'Chapecoense', 'Atlético-MG', 'Botafogo', 'Bahia', 'São Paulo', 'Fluminense', 
         'Sport Recife', 'EC Vitória', 'Coritiba', 'Avaí', 'Ponte Preta', 'Atlético-PR', 
         'Atlético-GO')
print(f'Lista de times do Brasileirão: {times}')
print('-=' * 20)
print(f'Os 5 primeiros times são: {times[0:5]}')
print('-=' * 20)
print(f'Os 4 últimos colocados são: {times[-4:]}')
print('-=' * 20)
print(f'O Chapecoense está na {times.index("Chapecoense") + 1}ª posição.')
 