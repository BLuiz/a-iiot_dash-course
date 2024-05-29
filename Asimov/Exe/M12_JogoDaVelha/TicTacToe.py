"""Projeto de jogo: Jogo da Velha"""
from uteis import *
from game_class import JogoDaVelha
from time import sleep
from os import system

# Definição do símbolo de cada jogador
players = dict()
players['you'] = valid_range("Símbolo: ", ['X','O'])
players['npc'] = 'X' if players['you'] == 'O' else 'O'

# Incializando o jogo
game = JogoDaVelha()

winner = False
while not winner:

    for symbol in players.values():
        system('cls')
        print(display_board(game.board))

        winner = game.endgame()
        

        if winner:
            if winner == ' ': print("Empatou")
            else: print("Ganhador: ", winner)
            break


# validar se os dois escolherem mesmo símbolo
# validar se o jogador escolher uma casa que já tem símbolo
