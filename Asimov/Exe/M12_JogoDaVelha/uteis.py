"""### Módulo de utitários para matrizes"""

def display_board(matrix):
    """Função para exibir o tabuleiro e o posicionamento de cada jogador
    :return: uma string que representa o tabuleiro
    """
    txt = str()
    for i, row in enumerate(matrix):
        for j, cell in enumerate(row):
            txt += f'  {cell}  '
            if j != 2: txt += '|'
        if i != 2: txt += '\n-----+-----+-----\n'
    return txt
def valid_place(text, error=False):
    """Função para tratar a entrada de dados referente às posições do jogo
    :param error: exibe uma mensagem de erro caso o último valor tenha sido invalidado (na recursividade)        
    :return: se o número estiver no interavalo [0,2] retorna ele mesmo. Se o programa for interrompido retorna -1
    """
    if error: print('Valor inválido!')
    try: inp = input(f'{text}')
    except KeyboardInterrupt: return -1
    else: return int(inp) if (inp in ['0','1','2']) else valid_place(text, True)
def valid_symbol(text, error=False):
    """Função para tratar a entrada de dados referente ao simbolo de cada jogador
    :param error: exibe uma mensagem de erro caso o último valor tenha sido invalidado (na recursividade)        
    :return: retorna uma string com o símbolo escolhido pelo jogador
    """
    if error: print('Valor inválido!')
    try: inp = input(f'{text}')
    except KeyboardInterrupt: return -1
    else: return inp if inp != ' ' else valid_place(text, True)
def tp_board(matrix):
    """Função para retornar a matriz trasposta do tabuleiro do jogo"""
    return list(zip(*matrix))
def first_diag(matrix):
    """Função para retornar os elementos da diagonal principal do tabuleiro"""
    return [row[i] for i, row in enumerate(matrix)]
def second_diag(matrix):
    """Função para retornar os elementos da diagonal secundária do tabuleiro"""
    return [row[abs(i-2)] for i, row in enumerate(matrix)]
