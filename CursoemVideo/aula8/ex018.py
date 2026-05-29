#Faca um programa que leia um angulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse angulo
import math
angle = float(input('Digite um angulo qualquer: '))
radAngle = math.radians(angle)
s = math.sin(radAngle)
c = math.cos(radAngle)
t = math.tan(radAngle)

print('O angulo é {:.0f}°.\nO sen{:.0f}° é {:.2f}.\nO cos{:.0f}° é {:.2f}.\nE a tan{:.0f}° é {:.2f}.'.format(angle, angle, s, angle, c, angle, t))
