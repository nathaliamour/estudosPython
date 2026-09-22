"""
Faça um programa que jogue par ou ímpar com o computador. O jogo será interrompido 
quando o jogador perder, mostrando o total de vitórias consecutivas que ele 
conquistou no final do jogo.
"""
from random import randint

vitorias = 0

while True:
    jogador = int(input("Digite um número: "))
    escolha = input("Par ou ímpar? [P/I]: ").strip().upper()

    computador = randint(0, 10)
    total = jogador + computador

    print(f"Você jogou {jogador} e o computador jogou {computador}.")
    print(f"Total: {total} — ", end="")

    if total % 2 == 0:
        resultado = "P"
        print("deu PAR.")
    else:
        resultado = "I"
        print("deu ÍMPAR.")

    if escolha == resultado:
        vitorias += 1
        print("Você venceu! Vamos jogar novamente.\n")
    else:
        print("Você perdeu!")
        break

print(f"Fim do jogo! Você conquistou {vitorias} vitória(s) consecutiva(s).")