from typing import Optional 
from models.produto_model import Produto 
from sql.produto_sql import SQL_CRIAR_TABELA, SQL_INSERIR, SQL_OBTER_TODOS 
from util import obter_conexao 
 
def criar_tabela(): 
    with obter_conexao() as conexao: 
        db = conexao.cursor() 
        db.execute(SQL_CRIAR_TABELA) 
 
 
def inserir(produto: Produto) -> Optional[Produto]: 
    with obter_conexao() as conexao: 
        db = conexao.cursor() 
        db.execute(SQL_INSERIR,  
            (produto.nome, 
            produto.descricao, 
            produto.estoque, 
            produto.preco, 
            produto.categoria)) 
         
        if db.rowcount > 0: # rowcount diz quantas linhas da tabela foram modicadas pelo comando SQL 
            produto.id = db.lastrowid # LASTROWID DO OBJETO DB É O ULTIMO ID QUE FOI GERADO PARA A TABELA 
            return produto 
        else: 
            return None 
     
def buscar_todos(): 
    with obter_conexao() as conexao: 
        db = conexao.cursor() 
        db.execute(SQL_OBTER_TODOS) 
        return db.fetchall()  # Retorna todos os registros

      