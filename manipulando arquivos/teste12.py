import os
from os import path
import shutil
from shutil import make_archive
from zipfile import ZipFile


def CriaZipModo1(): # criando função 
    shutil.make_archive("ArquivoCompactado", "zip", "C:\\Desktop\\Exercícios - Descubra o Python\\Ch3") # criando arquivo zip

#CriaZipModo1()

def CriaZipModo2():
    with ZipFile("ArquivoZipModo2.zip", "w") as novoZip: # controlar oq vamos incluir no arquivo zip
        novoZip.write("NovoArquivo.bkp") # indicando arquivos que fazem parte do zip
        novoZip.write("NovoArquivo.txt") 
        novoZip.write("zipModo1.zip.zip")

#CriaZipModo2()

def DeletaArquivo():
    os.remove("ArquivoZipModo2.zip")

DeletaArquivo()