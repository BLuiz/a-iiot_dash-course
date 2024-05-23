import pandas as pd                                     # Antes de importar: linha 4
from IPython.display import display                     # Antes de importar: linha 23

"""# Pandas é uma bibliteca formada por frameworks para manipulação de dados"""
'# Requer importação e é comumente importada com o apelido pd'

'# No DataOps, para tratamento dos dados com pandas, são utilizados os DataFrames'
# vazio_df = pd.DataFrame()                               # Declarando um dataframe vazio à uma variável

'# O método de criação também pode ser usado para converter uma estrutura nativa do python para um DF'
"""aux_compras = {                                         # Variável auxiliar de exemplo
    'data': ['25/03/2024', '26/03/2024'],
    'valor': [500, 300],
    'produto': ['feijão', 'arroz'],
    'quantidade': [50, 70]
}
compras_df = pd.DataFrame(aux_compras)"""                  # Dict -> DataFrame

'# Tabularizar dados que estão em um arquivo'
vendas_df = pd.read_excel('../Vendas.xlsx')             # Declarando

'# Para exibição no terminal, se utilizam dois métodos:'
# print(compras_df, end='\n\n')
# display(compras_df, end='\n\n')                       # Display não é nativo, requer instalação e importação

'# Alguns métodos uteis de visualização de dados:'
# display(vendas_df.head())
# print(vendas_df.shape)
# display(vendas_df.describe())

'# No DataOps, além dos DFs, as tabelas, existem as Series, que formam as tabelas e são apenas uma coluna de dados'
'# Ou seja, para o recorte de uma coluna específica:'
# produtos = vendas_df['Produto']
'# Para recortar mais de uma coluna'
# qtdXval = vendas_df[['Quantidade', 'Valor Unitário']]
'# Para o recorte de linhas, e/ou colunas ou condicionais:'
'# Metódo: var.loc[linhas, colunas]'
# rows = vendas_df.loc[1]                                           # Recorte de linha específica
# rows = vendas_df.loc[0:5]                                         # Recorte de linhas 0 a 5
# rows = vendas_df.loc[::-2]                                        # Recorte de IDs Pares e tabela inversa
# rows = vendas_df.loc[vendas_df['ID Loja'] == 'Iguatemi Campinas'] # Recorte condicional
# rows = vendas_df.loc[                                             # Recorte condicional de linhas e colunas
#    vendas_df['ID Loja'] == 'Iguatemi Campinas',  # rows
#    ["ID Loja", "Produto", "Valor Final"]  # cols
# ]
#display(rows)
'# Para Recortar uma célula específica: '
# cel = vendas_df.loc[1, 'Produto']

'# Criação de linhas e colunas'
'# De uma Coluna existente:'
# vendas_df['Comissão'] = vendas_df['Valor Final'] * 0.5
'# Uma nova Coluna:'
# vendas_df['Imposto'] = 0          # Inadequado
# vendas_df.loc[:, 'Imposto'] = 0   # Adequado
'# Adição de Linhas:'
# rows = pd.read_excel('../Vendas - Dez.xlsx')
# vendas_df = vendas_df._append(rows)

'# Exclusão de linhas e colunas'
'# Com o Método .drop() é necessário passar o eixo que se está excluindo: 0-Linha; 1-Coluna;'
# vendas_df = vendas_df.drop(["Valor Unitário", "Valor Final"], axis=1)
'# Utilizando o .dropna() para linhas/colunas que tenham valores vazios'
# vendas_df = vendas_df.dropna(how='all', axis=0)   # Exclui linhas com todas as células vazias
# vendas_df = vendas_df.dropna()                    # Exclui colunas com qualquer célula vazia

'# Métodos de preenchimento'
'# Preencher valores vazios: .fillna(), '           # .mean() -> média
# vendas_df['Comissão'] = vendas_df['Valor Final'] * 0.5
# vendas_df['Comissão'] = vendas_df['Comissão'].fillna(vendas_df['Comissão'].mean())
'# Preencher com o valor acima: .ffill()'
# vendas_df['Comissão'] = vendas_df['Comissão'].ffill()

'# Métodos de cálculo de indicadores:'
'# Contar e ordenar quantidade de aparecimentos de um valor em uma coluna'
# transacoes_loja = vendas_df['ID Loja'].value_counts()
'# Agrupar e somar valores'
# fat_loja = vendas_df[['ID Loja', 'Valor Final']].groupby('ID Loja').sum()
# qtd_produto = vendas_df[['Produto', 'Quantidade']].groupby('Produto').sum()
# display(fat_loja)
# display(qtd_produto)

'# Mesclar DataFrames'
# gerentes_df = pd.read_excel('../Gerentes.xlsx')
# vendas_df = vendas_df.merge(gerentes_df)
# display(gerentes_df)

# display(vendas_df)
