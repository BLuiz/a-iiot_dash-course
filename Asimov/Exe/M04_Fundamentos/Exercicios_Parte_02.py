def ex01_media():
    """ 
    1. Faça um programa para a leitura de duas notas parciais de um aluno. O programa deve calcular a média alcançada
    por aluno e apresentar:
    A mensagem "Aprovado", se a média alcançada for maior ou igual a 7;
    A mensagem "Reprovado", se a média for menor do que 7;
    A mensagem "Aprovado com Distinção", se a média for igual a 10. 
    """

    nota1 = float(input('Informe a primeira nota: '))
    nota2 = float(input('Informe a segunda nota: '))

    media = (nota1 + nota2) / 2

    if media > 10 or media < 0:
        print('Notas excedem 10, média inválida')
    else: 
        print(f'Média final: {media:.2f}.')
        
        if media == 10:
            print('Situação: Aprovado com Distinção!')
        elif media >= 7:
            print('Situação: Aprovado!')
        else:
            print('Situação: Reprovado!')


def ex02_maior_menor():
    """ 
    2. Escreva um script que leia três números e mostre o maior e o menor deles. 
    """
    maior = menor = 0

    for i in range(3):
        num = int(input(f'Informe {i+1}° número: '))
        
        if i == 0:
            maior = num
            menor = num
        if num > maior:
            maior = num
        if num < menor:
            menor = num

    print('Menor: ', menor)
    print('Maior: ', maior)


def ex03_escada_nome():
    """ 
    3. Nome na vertical em escada.
    """
    
    nome = str(input('Informe seu nome: '))

    for i in range(len(nome)):
        for j, letra in enumerate(nome):
            print(letra, end='')
            if j==i:
                break
        print()

    # for i in range(len(nome) + 1):
    #     print(nome[:i])


def ex04_fibonacci():
    """ 
    4. A série de Fibonacci é formada pela seqüência 1,1,2,3,5,8,13,21,34,55,... (o próximo termo, a partir do
    terceiro, é sempre gerado a partir do somatório dos últimos dois). Faça um programa capaz de gerar a série até o
    n-ésimo termo (onde o valor n deve ser inserido pelo usuário). 
    """ 
    
    seq = list()
    sum = aux = 0
    num = 1

    lim = int(input('Informe o limite da sequência fibonacci: '))

    for i in range(lim):
        sum = num + aux
        seq.append(sum)
        # print(f'num:{num}\t\taux:{aux}\t\tsum:{sum}')
        aux = num
        num = sum
    print(seq)


def ex05_valida():
    """ 
    5. Faça um programa que leia e valide as seguintes informações:
    Nome: maior que 3 caracteres;
    Idade: entre 0 e 150;
    Salário: maior que zero;
    Sexo: 'f' ou 'm';
    Estado Civil: 's', 'c', 'v', 'd';
    """

    def valida(categoria, revalida=False):
        if revalida: print(f'{categoria.split()[0]} Inválida(o)!')
        
        aux = input(f'{categoria}:')
        
        if 'Nome' in categoria:
            # Tratamento de dado
            nome=''
            for word in aux.title().split():
                nome += word
            # Validação
            if len(nome) > 3: return nome
            else: return valida('Nome', True)
        
        elif 'Idade' in categoria:
            # Tratamento de dado
            idade = int(aux)
            # Validação
            if (0< idade < 150): return idade
            else: return valida('Idade', True)
        
        elif 'Salário' in categoria:
            # Tratamento de dado
            salario = float(aux)
            # Validação
            if salario > 0: return salario
            else: return valida('Salário', True)
        
        elif 'Sexo' in categoria:
            # Tratamento de dado
            sexo = aux.lower().lstrip()[0]
            # Validação
            if sexo == 'm': return 'Masculino'
            elif sexo == 'f': return 'Feminino'
            else: return valida('Sexo (f - Feminino | m - Masculino)', True)
        
        else:
            # Tratamento de dado
            estado = aux.lower().lstrip()[0]
            # Validação
            if estado == 's': return 'Solteira(o)'
            elif estado == 'c': return 'Casada(o)'
            elif estado == 'v': return 'Viúva(o)'
            elif estado == 'd': return 'Divorciada(o)'
            else: return valida('Estado Civil (s - Solteiro | c - Casado | v - Viúvo | d - Divorciado)', True)

    # Criação de validação
    dados = dict()
    
    # Validação de dados
    dados['Nome'] = valida('Nome')
    print('Nome válido.\n')
    dados['Idade'] = valida('Idade')
    print('Idade válida.\n')
    dados['Salário'] = valida('Salário')
    print('Salário válido.\n')
    dados['Sexo'] = valida('Sexo (f - Feminino | m - Masculino)')
    print('Sexo válido.\n')
    dados['Estado Civil'] = valida('Estado Civil (s - Solteiro | c - Casado | v - Viúvo | d - Divorciado)')
    print('Estado Civil válido.\n\n')

    # Exibição dos dados válidos
    for k, v in dados.items():
        print(f'{k}: {v}')


def ex06_primos():
    """ 
    6. Faça um programa que peça um número inteiro e determine se ele é ou não um número primo. Um número primo é
    aquele que é divisível somente por ele mesmo e por 1. Dica: Utilize o operador aritmético %, que retorna o resto da
    divisão de dois números. 
    """

    num = int(input('Informe um número inteiro: '))
    
    div = [(n) for n in range(num-1, 1, -1) if (num % n == 0)]
    
    if num < 2 or len(div) > 0:
        sit = f'{num} não é Primo, ele é divisível por {div}'
    else:
        sit = f'{num} é Primo!'
    print(sit)
