def ex01_imc():
    """
    1. Utilizando o built-in method input(), crie um programa que receba a altura e o peso de uma pessoa e imprima
    na tela o IMC da mesma.
    """

    height = float(input('Informe sua altura em metros: '))
    weight = float(input('Informe seu peso: '))

    imc = weight / (height ** 2)

    print(f'IMC: {imc:.2f}')


def ex02_cumprimentar():
    """
    2. Escreva um programa que pergunte o nome completo do usuário e cumprimente o mesmo pelo primeiro nome.
    """

    nome_comp = str(input('Qual é seu nome completo? '))    # capta nome
    prim_nome = nome_comp.capitalize().split()[0]           # insere maiúsculo na primeira letra e capta primeiro nome

    print(f'Olá {prim_nome}, como vai você?')


def ex03_email():
    """
    3. Desenho um código que extraia o domínio de um e-mail informado.
    """

    email = str(input('Informe seu email: '))

    index = email.find('@') + 1
    print('Domínio do email: ', email[index:])


def ex04_tintas():
    """
    4. Faça um programa para uma loja de tintas. A pessoa informa a área em m2 que deseja pintar,
    e o script calculará a quantidade de latas de tinta que a pessoa deve comprar e o valor.
    Considere que cada litro de tinta pinta 3m2, que cada lata contém 18L e que custa R$ 80.
    """

    # Definição do problema
    area = float(input('Informe a area em m²: '))
    m2_por_litro = 3
    litro_por_lata = 18

    # Rendimento de cada lata
    rendimento = m2_por_litro * litro_por_lata

    # Calculo da quatia de latas
    latas = int(area // rendimento)
    resto = bool((area / rendimento) - latas)
    qtd_latas = latas + resto

    # Calculo do valor
    custo = qtd_latas * 80

    print(f'Total latas: {qtd_latas}')
    print(f'Custo total: R${custo:.2f}')


def ex05_salario():
    """
    # 5. Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês.
    Calcule e mostre o total do seu salário no referido mês, sabendo-se que
    são descontados 11% para o Imposto de Renda, 8% para o INSS e 5% para o sindicato, faça um programa que nos dê:
    1. Salário bruto.
    2. Quanto pagou ao INSS.
    3. Quanto pagou ao sindicato.
    4. O salário líquido.
    """

    ganho_hora = float(input('Informe seu salário por hora: '))
    horas_trab = float(input('Informe quantas horas você trabalhou esse mês: '))

    sal_bruto = ganho_hora * horas_trab

    inp_renda = sal_bruto * 0.11
    inss = (sal_bruto - inp_renda) * 0.08
    sindi = (sal_bruto - inp_renda - inss) * 0.05

    sal_liqui = sal_bruto - (inss + sindi + inp_renda)

    print(f'1. Salário bruto: R${sal_bruto:.2f}')
    print(f'2. Quanto pagou ao INSS: R${inss:.2f}')
    print(f'3. Quanto pagou ao sindicato: R${sindi:.2f}')
    print(f'4. O salário líquido: R${sal_liqui:.2f}')
