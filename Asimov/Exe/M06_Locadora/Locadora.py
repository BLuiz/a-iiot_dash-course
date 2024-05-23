""" Projeto de uma Locadora """
from M06_Locadora.uteis import *
from os import system

carros = [
    {'Nome': 'Chevrolet Tracker',   'Valor': 120.0, 'Disponível': True},
    {'Nome': 'Chevrolet Onix',      'Valor': 90.00, 'Disponível': True},
    {'Nome': 'Chevrolet Spin',      'Valor': 150.0, 'Disponível': True},
    {'Nome': 'Hyundai HB20',        'Valor': 85.00, 'Disponível': True},
    {'Nome': 'Hyundai Tucson',      'Valor': 120.0, 'Disponível': True},
    {'Nome': 'Fiat Uno',            'Valor': 60.00, 'Disponível': True},
    {'Nome': 'Fiat Mobi',           'Valor': 70.00, 'Disponível': True},
    {'Nome': 'Fiat Pulse',          'Valor': 130.0, 'Disponível': True},
    {'Nome': 'Fusca aaaa',          'Valor': 55.00, 'Disponível': True},
    {'Nome': 'Bagatata',            'Valor': 150.0, 'Disponível': True},
]

tarefas = ['Visualização', 'Locação', 'Devolução',]

fluxo = ['Encerrar operações', 'Novas operações',]

alugar = ['Cancela', 'Confirma']

def loc():
    system('cls')

    continua = 1
    while continua:
        highlight('Locadora de carros Iniciada', symbol='=', size=40)

        # Capta tarefa
        display_op(tarefas, 'Opções de tarefas')
        op = get_op('O que deseja fazer?: ', 0, 2)

        system('cls')

        highlight(f'Nova operação: {tarefas[op]}', symbol='=', size=40)

        # Direcionando tarefa
        if op == 0:     # Visualização
            catalogo(carros, 'Catálogo', disp=True)
        elif op == 1:   # Locação
            catalogo(carros, 'Carros disponíveis para Locação', True)
            car_id = get_op('Qual carro deseja alugar?: ', begin=0, end=len(carros)-1)
            car = carros[car_id]
            if car['Disponível']:
                dias = get_op('Por quantos dias deseja alugar?: ', begin=1, end=365)
                nome = car['Nome']
                valor = f"R${(dias * car['Valor']):.2f}"
                display_op(alugar, f'Locação: {nome:<18} - {valor:>9}')
                confirm = get_op(f'Confirma a locação?: ', begin=0, end=1)
                if not confirm: print('Locação cancelada!')
                else:
                    set_available(carros, car_id, False)
                    print('Locação confimada!')
            else: print('Locação cancelada. Carro escolhido não foi devolvido ainda.')
        elif op == 2:   # Devolução
            catalogo(carros, 'Carros disponíveis para Devolução', False)
            car_id = get_op('Qual carro deseja devolver?: ', begin=0, end=len(carros)-1)
            car = carros[car_id]
            if not car['Disponível']:
                set_available(carros, car_id, True)
                print('Devolução confirmada.')
            else: print('Devolução cancelada. Carro escolhido não foi alugado ainda.')

        # Fluxo do sistema: encerrar/continuar
        display_op(fluxo, 'Tela de espera')
        continua = get_op('Informe a opção desejada: ', 0, 1)

        system('cls')
    
    highlight('Locadora de carros Encerrada', symbol='=', size=40)

