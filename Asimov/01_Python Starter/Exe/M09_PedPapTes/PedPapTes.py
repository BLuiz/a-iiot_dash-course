"""Projeto de jogo: Pedra Papel Tesoura"""
from M09_PedPapTes.uteis import *
from random import randint
from os import system

def ped_pap_tes():
    next = 0
    scout = {
        'Derrotas'  : 0,
        'Empates'   : 0,
        'Vitórias'  : 0,
    }
    game = [
        {'move': 'Pedra',     'win': lambda p: True if p==2 else False},
        {'move': 'Papel',     'win': lambda p: True if p==0 else False}, 
        {'move': 'Tesoura',   'win': lambda p: True if p==1 else False}, 
    ]
    
    while True:
        system('cls')

        # 2. Estatísticas
        if next == 2:
            highlight('Estatísticas de jogo', '=', 40)
            display_scout(scout)
            print('-'*40)
        
        # 1. Continuar
        else:
            highlight('Nova jogada', '=', 40)
            display_options(['Pedra', 'Papel', 'Tesoura'])

            # Definição das Jogadas
            npc = randint(0, 2)
            you = valid_ch('Sua jogada: ', inf=0, sup=2)
            if you == -1: break

            # Exibição de jogadas computadas
            print('-'*40)
            print('Computando jogadas: \n')
            print(f'NPC played: {game[npc]['move']}')
            print(f'You played: {game[you]['move']}\n')

            # Definição de vitória
            if npc==you: 
                print('Resultado: jogo empatou')
                scout['Empates'] += 1
            elif (game[you]['win'](npc)): 
                print('Resultado: jogador ganhou!')
                scout['Vitórias'] += 1
            else: 
                print('Resultado: jogador perdeu!')
                scout['Derrotas'] += 1
            print('-'*40, end='\n\n')

        # Continuidade do programa
        display_options(['Encerrar', 'Continuar', 'Estatísticas'])
        next = valid_ch('O que deseja fazer?: ', inf=0, sup=2)
        if -1 <= next <= 0: break
    
    system('cls')
    if (next == -1) or (you == -1): highlight('Jogo Interrompido', '=', 40)
    elif next == 0: highlight('Jogo Finalizado', '=', 40)
