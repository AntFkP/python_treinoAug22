from os  import path   # importar classe path do módulo os
import time

def DadosArquivo():
    # criar uma série de variáveis com informações provenientes da classe path
    ArquivoExiste = path.exists("NovoArquivo.txt") # verifica se o arquivo exixte 
    ehDiretorio = path.isdir("NovoArquivo.txt")  # verificar se é diretório 
    pathArquivo = path.realpath("NovoArquivo.txt")  # verificar qual o path do arquivo 
    pathRelativo = path.relpath("NovoArquivo.txt") #  verificar qual o path relativa 
    dataCriacao = time.ctime(path.getctime("NovoArquivo.txt")) # verificar data de criação do arquivo / utiliza classe time
    dataModificacao = time.ctime(path.getmtime("NovoArquivo.txt")) # verificar data de modificação do arquivo 

    print(ArquivoExiste)
    print(ehDiretorio)
    print(pathArquivo)
    print(pathRelativo)
    print(dataCriacao)
    print(dataModificacao)

DadosArquivo()