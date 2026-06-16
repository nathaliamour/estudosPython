"""
Faca um programa que mostre na tela uma contagem regressiva para estouro de fogos de artifício, indo de 10 até 0, 
com uma pausa de um segundo entre eles.
"""
import time
print("Contagem regressiva para estouro dos fogos!!!")
for i in range(10, 0, -1): 
    print(i)
    time.sleep(1)
print("\n    * . *\n    *  X  *\n    * . *")
time.sleep(1)
print("\n   \  |  /\n  --  *  --\n   /  |  \ ")
time.sleep(1)
print("\n     .  :  .\n   :  ' : '  :\n  .  *  X  *  .\n   :  . : .  :\n     '  :  '")
