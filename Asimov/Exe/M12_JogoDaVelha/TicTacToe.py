"""Projeto de jogo: Jogo da Velha"""
from uteis import *
from game_class import JogoDaVelha
from time import sleep
from os import system

# Definição do símbolo de cada jogador
players = dict()
players['you'] = valid_symbol("Informe o símbolo desejado para você: ")
players['npc'] = valid_symbol("Informe o símbolo desejado para o computador: ")


while True:
    
    # Incializando o jogo
    game = JogoDaVelha()

    print(display_board(game.board))

    for symbol in players.values:
        display_board(game.board)

        winner = game.endgame()

        if not winner: continue
        elif winner == ' ': print("Empatou")
        else: print("Ganhador: ", winner)

