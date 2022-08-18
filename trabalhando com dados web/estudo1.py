import urllib.request

def ConectaInternet():
    objUrl = urllib.request.urlopen("http://www.google.com")  # objeto vai armazenar o retorno de urllib.request.urlopen
# função urlopen vai tentar fazer a conexão com o site que passamos como parâmetro 
    if objUrl.getcode() == 200: # verificar se a conxção ocorreu 
        dados = objUrl.read()
        print(dados)

ConectaInternet()
