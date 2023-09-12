# Importa a blibioteca do MySQL
import mysql.connector

# Faz a conexão com o BD
conexao = mysql.connector.connect(
    host='localhost',
    user='root',
    password='',
    database='teste'
)

cursor = conexao.cursor()

# CRUD

# Cria tabela
criaTabela = 'CREATE TABLE PYTHON (coluna char);'
cursor.execute(criaTabela)
conexao.commit()

# Finaliza a conexão do BD
cursor.close()
conexao.close()