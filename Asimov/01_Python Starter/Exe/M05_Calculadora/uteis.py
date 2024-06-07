""" Módulo de Funções para Calculadora """

def print_menu(menu):
    """
    Função para mostrar ao usuário uma sequência de operações definidas a partir de um dicionário.
    
    :param menu: passagem de um dicionário de operações
    """

    for k, v in menu.items():
        print(f'({k}) - {v['Nome']}')
    print()


def get_op(menu, question, invalida=False):
    """
    Função para validar uma operação para cálculos. Funciona de maneira recursiva.
    
    :param menu: passagem de um dicionário de operações
    :param question: pergunta que se realia para o usuário
    :param invalida: utilizado para mostrar ao usuário que o último valor era inválido
    :return: retorna um caracter, valor tipo string de uma casa, que pertença ao dicionário de operações
    """
    
    if invalida: print('Operação inválida')

    print(question, end='')
    op = input().strip()[0]
    
    if (op in menu.keys()) or (op == '#'): return op
    else: return get_op(menu, question, invalida=True)


def highlight(text, symbol, size):
    """
    Função para destacar alguma string, um título ou subtítulo como um header/footer
    """
    print(f'{symbol}'*size)
    print(f'{text:^{size}}')
    print(f'{symbol}'*size)
    print()
