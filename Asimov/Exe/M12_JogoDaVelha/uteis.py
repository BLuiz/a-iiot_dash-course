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

def valid_range(text, scope, exception=-1, error=False):
    """Função para tratar a entrada de dados referente às posições do jogo
    :param text: string exibida perguntar o input
    :param scope: escopo de valores que se deve validar
    :param exception: valor retornado ao encontrar excessão
    :param error: exibe uma mensagem de erro caso o último valor tenha sido invalidado
    :return: string com o input recebido
    """

    if error: print('Input inválido!')

    try: inp = input(f'{text}')
    except KeyboardInterrupt: return exception
    else: return inp if inp in scope else valid_range(text, scope, exception, error=True)


# def valid_symbols(text, error=False):
#     """Função para tratar a entrada de dados referente ao simbolo de cada jogador
#     :param error: exibe uma mensagem de erro caso o último valor tenha sido invalidado (na recursividade)        
#     :return: retorna uma string com o símbolo escolhido pelo jogador
#     """
#     symb = list()
#     while len(symb)<=2:
#     if error: print('Símbolo inválido!')
#     try: inp = input(f'{text}')
#     except KeyboardInterrupt: return -1
#     else: return inp if inp != ' ' else valid_symbols(text, True)


def transpose_matrix(matrix):
    """Função para retornar a matriz trasposta do tabuleiro do jogo"""
    return list(zip(*matrix))
def first_diag(matrix):
    """Função para retornar os elementos da diagonal principal do tabuleiro"""
    return [row[i] for i, row in enumerate(matrix)]
def second_diag(matrix):
    """Função para retornar os elementos da diagonal secundária do tabuleiro"""
    aux = len(matrix) - 1 
    return [row[abs(i-aux)] for i, row in enumerate(matrix)]
