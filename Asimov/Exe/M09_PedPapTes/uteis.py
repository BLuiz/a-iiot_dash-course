from os import system
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


def display_options(options):
    """
    Função para exibição das possíveis jogadas do jogador
    :param options: lista de opções para serem exibidas
    """
    
    for i, op in enumerate(options):
        print(f'{i} - {op:>36}')


def display_scout(scout):
    """
    Função para exibição das estatísticas das jogadas anteriores
    :param scout: lista com cada categoria da estatística
    """
    
    for key, value in scout.items():
        tam = 40 - len(str(value))
        print(f'{key:<{tam}}{value}')


def valid_ch(text, inf, sup):
    """
    Função para validar inputs numéricos, considerando erros por interrupção de input, por conversão de tipo do input, e por intervalo do input.
    :param text: pergunta a ser exibida ao usuário
    :param inf: limite inferior do intervalo que o input numérico deve estar
    :param inf: limite superior do intervalo que o input numérico deve estar
    """
    
    while True:
        print(text, end='')
        try:
            num = int(input())
            assert (inf <= num <= sup)
        except AssertionError:      print(f'{num} não está nas opções')
        except ValueError:          print('Você não digitou um número.')
        except KeyboardInterrupt:   return -1
        else:                       return num
