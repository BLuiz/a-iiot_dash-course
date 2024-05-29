"""### Construção da base para o jogo"""

from uteis import *

class JogoDaVelha():
    def __init__(self):
        self.board = [
            [' ', ' ', ' '], 
            [' ', ' ', ' '], 
            [' ', ' ', ' ']
        ]

        self.board = {k:' ' for k in range()}


    def set_move(self, symbol, place):  ###
        """Função para registrar uma jogada no tabuleiro,por meio do local e o símbolo
        
        :param symbol: simbolo que cada jogador insere no tabuleiro
        :param place: uma tupla que informa a posição em que está sendo jogado. (row, col)
        """
        
        
        self.board[place[0]][place[1]] = symbol

    def endgame(self):
        """Função para verificar vencedor da partida

        :return: símbolo de quem ganhou a partida
        """
        # Se ainda houver células vazias o jogo deve continuar
        for row in self.board:
            for cell in row:
                if cell == ' ': return False

        # Caso contrário, todas as células estejam ocupadas:
        # Verifica vendedor nas diagonais
        stD = first_diag(self.board)
        if len(set(stD)) == 1: return stD[0]
        ndD = second_diag(self.board)
        if len(set(ndD)) == 1: return ndD[0]
        # Verifica vencedor nas linhas e colunas
        rgB = self.board
        tpB = transpose_matrix(self.board)
        for i in range(3): 
            if len(set(rgB[i])) == 1 or len(set(tpB[i])) == 1: return stD[i]
        return ' '
