def leituraArquivo(): # função para ler arquivo
    arquivo = open ("NovoArquivo.txt", "r")  # informar nome do arquivo / nome de acesso do arquivo r --> read
    if (arquivo.mode == "r"):  # validação para ver se está aberto no  modo de leitura 
        # ou seja só vou continuar caso o arquivo esteja no modo read 
        conteudo = arquivo.read() # variável conteúdo / metodo read 
        print (conteudo)

    arquivo.close()

#leituraArquivo()

def leituraArquivoGrande():
    arquivo = open ("NovoArquivo.txt", "r")
    if (arquivo.mode == "r"):
        conteudoTotal = arquivo.readlines()

        for conteudo in conteudoTotal: # loop para ler todas as linhas 
            print (conteudo)

    arquivo.close()

leituraArquivoGrande()