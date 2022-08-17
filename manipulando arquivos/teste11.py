import os
from os import path
import shutil # módulo shutil 

def copiaArquivo():  # função para copiar arquivo 
    if path.exists("NovoArquivo.txt"): # verificar se o arquivo existe 
        pathAtual = path.realpath("NovoArquivo.txt") # salvar path do arquivo em uma variável 
        novoPath = pathAtual + ".bkp" 
        shutil.copy(pathAtual, novoPath)  # método copy / dois parametros origem e destino dos arquivos 

        shutil.copystat(pathAtual, novoPath) 

#copiaArquivo()

def renomearArquivo(): # renomear o arquivo criado 
    if path.exists("NovoArquivo.txt.bkp"): # verificar se o arquivo existe 
        os.rename("NovoArquivo.txt.bkp", "ArquivoAlterado.txt")   # renomeando arquivos 

renomearArquivo()