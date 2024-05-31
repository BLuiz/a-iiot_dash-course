"""### Construção da base para o jogo"""

from uteis import *

class JogoDaVelha():
    def __init__(self):
        self.board = [
            {0:' ', 1:' ', 2:' '}, 
            {3:' ', 4:' ', 5:' '}, 
            {6:' ', 7:' ', 8:' '}, 
        ]

    def set_move(self, symbol, place):
        """Função para registrar uma jogada no tabuleiro,por meio do local e o símbolo
        :param symbol: simbolo que cada jogador insere no tabuleiro
        :param place: uma tupla que informa a posição em que está sendo jogado. (row, col)
        """
        # False se o lugar estiver ocupado
        if self.board[place // 3][place] != ' ': return 0
        # Caso contrário, True, realizando jogada
        self.board[place // 3][place] == symbol
        return 1


    def endgame(self):
        """Função para verificar vencedor da partida
        :return: símbolo de quem ganhou a partida
        """
        # Se ainda houver células vazias o jogo deve continuar
        if any(v==' ' for v in self.board.values()): return 0
        
        # Vendedor nas diagonais
        diag1 = first_diag(self.board)
        if len(set(diag1)) == 1: return diag1[0]
        diag2 = secnd_diag(self.board)
        if len(set(diag2)) == 1: return diag2[0]

        # Caso contrário, verifica qual venceu
        for i in range(len(board)):
            # Vencedor nas linhas
            row = (board[i]).values()
            if len(set(row))==1: return list(set(row))[0]
            # Vencedor nas colunas
            col = transpose_board(board)[i]
            if len(set(col))==1: return list(set(row))[0]
        
        # Caso não houve vencedor, retorna vazio para sinalizar empate
        return ' '
    

    def display_board(self):
        """Função para exibir o tabuleiro e o posicionamento de cada jogador. Funciona apenas com uma matriz composta de dicionários dentro de uma lista
        :return: uma string que representa o tabuleiro
        """
        txt = str()
        for i, row in enumerate(self.board):
            for k, v in row.items():
                txt += f'  {v}  '
                if k % 3 != 2: txt += '|'
            if i != 2: txt += '\n-----+-----+-----\n'
        return txt
    
        for key, value in self.board.items():
            txt += f'  {value}  '
            if key % 3 != 0: txt += '|'
            elif key != len(self.board): txt += '\n-----+-----+-----\n'


board = [
    {0:' ', 1:'O', 2:' '}, 
    {3:'X', 4:'O', 5:'X'}, 
    {6:' ', 7:'O', 8:' '}, 
]
