#ANSI - escape sequence
#.       \033[0;33;44m
#STYLE;         TEXT;               BACK
#                                   mesmas cores, porem
#0              30 - branco         40
#1 bold         31 - vermelho       41
#4 underline    32 - verde          42
#7 negative     33 - amarelo        43
#               34 - azul           44
#               35 - lilas          45
#               36 - ciano          46
#               37 - cinza          47

#\033[0;30;41m     \033[m
#\033[4;33;44m    \033[m
#\033[1;35;43m    \033[m
#\033[30;42m    \033[m
#\033[m    \033[m
#\033[7;30m     \033[m #inverte cor da letra e fundo

'''
frase = "A vida é bela"
cores = {'limpa':'\033[m',
        'azul':'\033[34m, 
        'amarelo':'\033[33m', 
        'pretoebranco':'\033[7;30m]'} 

print("A frase escolhida é {}{}{}!!!".format(cores['pretoebranco'], frase, cores['amarelo'])
'''


