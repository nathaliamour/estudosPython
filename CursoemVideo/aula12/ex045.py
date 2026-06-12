"""
Crie um programa que faça o computador jogar jokenpô com vc
"""
import random
player = int(input("\nVamos jogar jokenpo!!!\n\nVocê precisa escolher um número, dentre as opções abaixo:\n" \
"[1] Pedra\n[2] Papel\n[3] Tesoura\n\nQual a sua escolha? "))

jogadas = {
    1: "Pedra",
    2: "Papel",
    3: "Tesoura"
}
print("\nJO")
print("KEN")
print("PO!!!\n")

pc = random.randint(1, 3)

print("O computador jogou {}".format(jogadas[pc]))
print("O jogador jogou {}\n".format(jogadas[player]))

if pc == player: 
    print("Vocês empataram!!! \n Jogue novamente!")
elif (pc == 1 and player == 2) or (pc == 2 and player == 3) or (pc == 3 and player == 1):
    print("O JOGADOR venceu!!!")
else: 
    print("O COMPUTADOR venceu!!!")
