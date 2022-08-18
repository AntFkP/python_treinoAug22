from html.parser import HTMLParser

class meuParser(HTMLParser): # criando uma classe que vai herdar métodos da classe HTMLParser
    def handle_starttag (self, tag, attrs): # verifica se foi encontrado uma tag de abertura  / 3 pametros
        print("Tag de abertura encontrada!")
        if attrs.__len__() > 0:  # verificar se attrs tem valor   
            for a in attrs:  # loop para imprimir cada valor do attrs 
                print ("  Valores encontrados: ", a[0], " = ", a[1])  # variável a é um array 

    def handle_endtag(self, tag):
        print("Tag de fechamento encontrada")

    def handle_comment(self, data):  # verificar se algum método foi encontrado 
        print ("Comentário encontrado.")

    def handle_data(self, data):  # verificar se valores foram encontrados 
        print("Valores encontrados.")  # escrever na tela q algum valor foi encontrado 
        if data.isspace(): # verificar se o valor encontrado é um espaço
            print("O valor encontrado é um espaço")
        else:
            print("O valor encontrado é: ", data)   # passando como parametro o valor q foi encontrado 

def meuObjeto():  # função q vai instanciar um objeto do tipo meuParser
    meuparser1 = meuParser()
    arquivo = open("exemplohtml.html", "r")  # p/ abrir o arquivo 
    dados = arquivo.read()  # abrir arquivo para leitura
    meuparser1.feed(dados)

meuObjeto()