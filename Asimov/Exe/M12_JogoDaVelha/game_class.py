"""### Construção da base para o jogo"""

from M12_JogoDaVelha.uteis import *

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
        # Falha se o lugar estiver ocupado
        if self.board[place // 3][place] != ' ': return False
        
        # Caso contrário, realizando jogada
        self.board[place // 3][place] = symbol
        return True

    def endgame(self):
        """Função para verificar vencedor da partida
        :return: símbolo de quem ganhou a partida
        """

        is_filled = lambda seq: seq != ' ' 

        # Vendedor nas diagonais
        diag1 = first_diag(self.board)
        if len(set(diag1)) == 1 and is_filled(diag1[0]): return diag1[0]
        diag2 = secnd_diag(self.board)
        if len(set(diag2)) == 1 and is_filled(diag2[0]): return diag2[0]

        for i in range(len(self.board)):
            # Vencedor nas linhas
            row = (self.board[i]).values()
            if len(set(row)) == 1 and is_filled(list(set(row))[0]): return list(set(row))[0]
            # Vencedor nas colunas
            col = transpose_board(self.board)[i]
            if len(set(col)) == 1 and is_filled(list(set(col))[0]): return list(set(col))[0]
        
        # Caso não houve vencedor e todos os lugares estejam ocupados, retorna vazio para sinalizar empate
        if len(self.playable_places()) == 0: 
            print('Nenhum lugar disponível')
            return ' '

        # Se ainda houver células vazias o jogo deve continuar
        print('Células disponíveis ainda')
        return False
    
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
    
    def playable_places(self):
        """Função para retornar as chaves dos lugares disponíveis para jogada"""
        playable = list()
        for row in self.board: 
            playable += [k for k, v in row.items() if v==' ']
        return playable

