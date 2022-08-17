class minhaClasse():
    def __init__(self):  # método construtor
        self.meuAtributo = "Passou pelo construtor!" 

    def meuMetodo(self):  # executa uma ação
        print("Passou pelo meuMetodo")  #
    
    def meuMetodo2(self, valor):  # recebendo parametro  / recebe objeto self e um valor 
        self.outroAtributo = valor  # recebe 
        print(self.outroAtributo)

def criaObjeto(): # criar objeto para classe 
    meuObj = minhaClasse()  # instânciando objeto do tipo minhaClasse 
    var1 = meuObj.meuAtributo  # atribuir para a variável o valor de var1
    print(var1)

    meuObj.meuMetodo() # executar o método 

    meuObj.meuMetodo2("Executando um método") # executar o método 2 , passando um parametro

criaObjeto()