""" Módulo de Funções para Locadora """


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


def display_op(options, title):
    """
    Função para mostrar ao usuário sequências de opções para escolher.
    
    :param options: uma lista de opções que será mostrada
    :param title: título da sequência de opções
    """
    highlight(title, '-', 40)
    for i in range(len(options)):
        print(f'[{i}] - {options[i]:<34}')
    print('-'*40)
    print()


def get_op(question, begin=0, end=1, invalid=False):
    """
    Função para validar uma opção disponibilizada pelo sistema.
    
    :param question: 
    :param begin: limite inferior em que os números devem estar para ser válidos 
    :param end: limite superior em que os números devem estar para ser válidos 
    :param invalid: informa se algum dado já foi invalidado para mostrar ao usuário mensagem de erro
    :return: opção validada entre os limites inferior e superior
    """
    if invalid: print('Operação inválida')

    # Entrada: continuar/encerrar
    print(question, end='')
    op = int(input())

    # Recursividade para validação
    if (begin <= op <= end): return op
    else: return get_op(question, begin, end, True)


def catalogo(menu, title, disp=True):
    """
    Função para mostrar ao usuário os carros do catálogo.
    
    :param menu: uma lista ou dicionário com as opções
    :param title: título da listagem de itens do menu
    :param disp: mostrar apenas os carros disponíveis ou não
    """

    highlight(title, '-', 40)

    for i, car in enumerate(menu):
        if (disp == car['Disponível']):
            nome = car['Nome']
            valor = f"R${car['Valor']:.2f}"
            print(f'[{i}] {nome:<18} - {valor:>9} / dia')


def set_available(menu, id, value):
    """
    Função inverter a situação de cada carro, seja de alugado para devolvido e vice-versa

    :param menu: uma lista ou dicionário com os carrros
    :param id: index em que o carro se encontra no menu
    :param value: valor (true/false) a ser inserido no campo de disponibilidade
    """
    for i, car in enumerate(menu):
        if i == id:
            car['Disponível'] = value
