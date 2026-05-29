#bibliotecas
#biblioteca math - ceil/floor/trunc/pow/sqrt/factorial
#duas maneiras de usar - 1. import math -- importa tudo da biblioteca
#2. from math import sqrt -- só estarei podendo usar o sqrt da biblioteca math

import math
num = int(input('Digite um número: '))
raiz = math.sqrt(num)
print('A raiz de {} é igual a {}'.format(num, math.ceil(raiz)))
