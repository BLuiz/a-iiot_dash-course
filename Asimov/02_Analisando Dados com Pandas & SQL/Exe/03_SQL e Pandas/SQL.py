import sqlite3
import pandas as pd
from IPython.display import display

""" ## Criação de Connection Engine -  """
conn = sqlite3.connect('web.db')

""" ## Importação da base de dados """
df_data = pd.read_csv('..\\..\\Docs\\Analisando Dados com Pandas & SQL\\SQL & Pandas\\bd_data.csv', index_col=0)

""" ## Exportação para DB """
df_data.index.name = 'index_name'
# df_data.to_sql('data', conn, index_label='index_name')

""" ## Postagem de atualizações no banco de dados, caso necessário """
# conn.commit()

""" ## Criação de um cursor para enviar comandos SQL"""
c = conn.cursor()

""" ## CREATE """
# c.execute('''CREATE TABLE products (
#         [product_id] INTEGER PRIMARY KEY, 
#         [product_name] TEXT, 
#         [price] INTEGER)
# ''')

""" ## DROP """
# c.execute('DROP TABLE products')
# c.execute('DROP TABLE data')

""" ## INSERT - SQL """
# c.execute('''INSERT INTO products (product_id, product_name, price) VALUES 
#           (0, 'Computer', 800),
#           (1, 'Printer', 200),
#           (2, 'Tablet', 300);
# ''')
# conn.commit()

""" ## INSERT - Pandas """
# df_data2 = df_data.iloc[::-2]
# df_data2.to_sql('data', conn, if_exists='append')

""" ## SELECT - SQL """
# c.execute('SELECT * FROM data')
# c.execute('''SELECT A, B, C FROM data WHERE A > 200 AND A < 230''')
# display(c.fetchall())

""" ## SELECT - Pandas """
# query = 'SELECT * FROM data'
# df = pd.read_sql(query, con=conn, index_col='index_name')
# display(df)

""" ## UPDATE """
# c.execute('UPDATE data SET A=0, B=245 WHERE index_name=1')
# conn.commit()

""" ## DELETE """
# c.execute('DELETE FROM data WHERE index_name=1')
# conn.commit()

