"""Projeto de jogo: Jogo da Velha"""
from M12_JogoDaVelha.uteis import *
from M12_JogoDaVelha.game_class import JogoDaVelha
from os import system
from random import choice

def tictactoe():
    # Incializando o jogo
    game = JogoDaVelha()

    # Definição de símbolo dos jogadores e ordem de jogadas
    you_symbol = valid_range("Símbolo: ", ['X','O'])
    if you_symbol == -1: print('SAIR DO JOGO')
    whose_turn = choice([0, 1])


    # Criação de dicionário auxiliar
    menu = [
        {'player': 'you', 'symbol': you_symbol}, 
        {'player': 'npc', 'symbol': 'X' if you_symbol=='O' else 'O'}, 
    ]

    winner = False
    while not winner:

        # Exibe o tabuleiro
        print(game.display_board())

        lim = game.playable_places()

        # Escolha de qual lugar jogar
        if menu[whose_turn]['player'] == 'npc': 
            place = choice(lim)
        else: 
            place = int(valid_range("Jogada [0 a 8]: ", [str(i) for i in lim]))
            if place == -1: break

        # Realiza jogada e verifica se houve vencedor
        game.set_move(menu[whose_turn]['symbol'], place)

        # Controle do próximo jogador
        if whose_turn: whose_turn = 0
        else: whose_turn = 1
        
        # Verifica se o jogo terminou e quem ganhou
        winner = game.endgame()
        
        # Limpa a tela
        system('cls')

    # Se o jogo Finalizou normalmente, exibe vencedor
    else: 
        highlight('Jogo Finalizado', '=', 40)
        if winner == ' ': print("Empatou")
        else: print("Ganhador: ", winner)

    # Se o jogo o jogo tenha sido interrompido
    if place == -1:
        system('cls')
        highlight('Jogo interrompido', '=', 40)
