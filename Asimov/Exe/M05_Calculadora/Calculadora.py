""" Projeto de uma Calculadora """
from M05_Calculadora.uteis import get_op, print_menu, highlight
from os import system


def calc():
    """
    Função para calcular operações entre dois números. Função principal, porém engloba funções de visualização e validação.
    """
    
    # Definição de operações
    operacoes = {
    '+': {'Nome': 'Adição',         'Calc': lambda n1,n2: n1 + n2},
    '-': {'Nome': 'Subtração',      'Calc': lambda n1,n2: n1 - n2},
    '*': {'Nome': 'Multiplicação',  'Calc': lambda n1,n2: n1 * n2},
    '/': {'Nome': 'Divisão',        'Calc': lambda n1,n2: n1 / n2},
    '^': {'Nome': 'Exponenciação',  'Calc': lambda n1,n2: n1 ** n2}
    }

    while True:
        highlight('Calculadora Iniciada', symbol='=', size=40) 
        print_menu(operacoes)

        # Entrada: operação válida
        op = get_op(menu=operacoes, question='Operação (# - Sair): ')

        # Limpando a tela
        system("cls")

        # Operações
        if op == '#': break
        
        highlight(f'Nova operação: {operacoes[op]['Nome']}', symbol='-', size=40)

        # Entrada: números
        n1 = float(input('1° Número: '))
        n2 = float(input('2° Número: '))
        
        # Cálculo
        res = operacoes[op]['Calc'] (n1, n2)
        
        # Saída: resultado
        print(f'{n1:.2f} {op} {n2:.2f} = {res:.2f}\n')

    highlight('Calculadora encerrada', symbol='=', size=40)
