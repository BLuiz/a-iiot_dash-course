"""## Módulo de utitários desenvolvidos durante o curso"""


def highlight(text, symbol, size):
    """
    Função para destacar alguma string, um título ou subtítulo como um header/footer

    :param text: a string que será destacada
    :param symbol: o síbolo de destaque para a string
    :param size: tamanho do header de destaque, considerando os símbolos e o centralizar do texto
    """
    # Display de um título em header
    print(f'{symbol}'*size)
    print(f'{text:^{size}}')
    print(f'{symbol}'*size)
    print()


def valid_range(text, scope, e=-1, error=False):
    """Função para tratar a entrada de dados referente às posições do jogo
    :param text: string exibida perguntar o input
    :param scope: escopo de valores que se deve validar
    :param e: valor retornado ao encontrar excessão
    :param error: exibe uma mensagem de erro caso o último valor tenha sido invalidado
    :return: string com o input recebido
    """
    if error: print('Input inválido!')
    try: inp = input(f'{text}')
    except KeyboardInterrupt: return e
    else: return inp if inp in scope else valid_range(text, scope, e, error=True)


def transpose_board(board):
    """Função para retornar a matriz trasposta do tabuleiro do jogo"""
    if type(board[0]) == dict: aux = [ row.values() for row in board]
    else: aux = board
    return list(zip(*aux))

def first_diag(board):
    """Função para retornar os elementos da diagonal principal do tabuleiro"""
    size = len(board) + 1
    return [row[(i * size)] for i, row in enumerate(board)]

def secnd_diag(board):
    """Função para retornar os elementos da diagonal secundária do tabuleiro"""
    size = len(board ) - 1
    return [row[(i+1) * size] for i, row in enumerate(board)]

def isEven(num):
    return (num % 2) == 0
