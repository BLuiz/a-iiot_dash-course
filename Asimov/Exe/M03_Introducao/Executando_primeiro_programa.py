def ex01_print():
    """ 
    Testando códigos
    """
    print('Olá, Mundo!')


def ex02_input():
    """ 
    Testando códigos
    """
    print('Digite sua idade: ')
    valor = input()
    print('Você possui {}'.format(valor))


def ex03_pares():
    """ 
    Testando códigos
    """
    import pandas as pd

    # df = pd.read_csv("supermarket_sales.csv")
    # df.columns
    # df["Unit Price"].sum()

    a = []
    for i in range(0, 10):
        if (i % 2) == 0:
            print(i)

    print('Hello, World!')
