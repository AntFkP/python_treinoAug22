

def EscreveArquivo():
    
    arquivo = open("NovoArquivo.txt", "w+") # w significa que vamos escrever no arquivo / + significa que se o arquivo não existe ele é criado
    # open abre o arquivo
    arquivo.write("LInha gerada com a função 'escreve arquivo' \r\n")
    # write escreve no arquivo 
    arquivo.close() # para fechar o arquivo 

# EscreveArquivo()

def AlteraArquivo():
    arquivo = open("NovoArquivo.txt", "a+") # w significa que vamos escrever no arquivo / + significa que se o arquivo não existe ele é criado
    arquivo.write("LInha gerada com a função 'altera arquivo' \r\n")

    arquivo.close() # para fechar o arquivo 

AlteraArquivo()