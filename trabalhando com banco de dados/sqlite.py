import sqlite3 # importar módulo sqlite3 --> possui as classes necessárias para trabalharmos com o banco de dados Sqlite 

def manipulaDados(bancoDados, comando): # informar qual banco de dados vai ser utilizado e qual comando 
    conexao = sqlite3.connect(bancoDados) # criar um objeto que faz conexão do sqlite com o bando de dados
    cursor = conexao.cursor() # cursor responsável pela execução do comando  / criando objeto do tipo cursor
    cursor.execute(comando) # execute recebe como parametro comando
    conexao.commit()  # efetivar as alterações com o método comit 
    conexao.close()  # fechar a conxeão com o sqlite

def selecionaDados(bancoDados, comando): # função para fazer update no banco de dados 
    # recebe como paramentro o bancoDados e o Comando 
    conexao = sqlite3.connect(bancoDados) # conectar banco de dados c/ sqlite 
    cursor = conexao.cursor() # cursor responsável pela execução do comando  / criando objeto do tipop cursor
    cursor.execute(comando) # execute recebe como parametro comando
    linhas = cursor.fetchall() # função fetch all para buscar linhas q estão retornando para o comando 
  # objeto linha --> para buscar todas as linhas retornadas pelo comando 
    for linha in linhas:  # para exibir as linhas no console 
        print(linha)

def ManipulacaoDados():  # para manipular nosso banco de dados 
    comandoInsert = "INSERT INTO estados (nome_estado, sigla_estado, nome_capital) VALUES ('Estado Teste', 'XX', 'Teste Inclusão')"
   # comando insert para inserir dados na tabela --> p/ isso vc precisa conhecer a estrutura dela 
    pathBD = "BancoDeDados.db"  # path do bando de dados 
    comandoSELECT = "SELECT nome_estado, sigla_estado, nome_capital FROM estados"

    manipulaDados(pathBD, comandoInsert)
    selecionaDados(pathBD, comandoSELECT)

ManipulacaoDados()