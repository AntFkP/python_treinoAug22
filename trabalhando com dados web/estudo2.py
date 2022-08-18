import urllib.request  
import json  # módulo json com a classes para manipularmos Json

def ManipulaJSON():  # criando função
    endereco = "https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/2.5_day.geojson"  # variável com o endereço do site 
    webURL = urllib.request.urlopen(endereco)  # criando o objeto / parametro variável endereço
    if (webURL.getcode() == 200):   # verificando se o ocorreu a conexão
        dados = webURL.read()   # carregar em uma variável os dados da página 
        oJSON = json.loads(dados)  # objeto json com o conteúdo dessa página, mas no formato Json
        #Criar dicionário --> dicionário = conjunto de dados --> chaves 

        contagem = oJSON["metadata"]["count"]  # variável contagem chave metadata  e dentro da chave metada estamos procurando a chave count 
        print ("Contagem: " + str(contagem))

        for local in oJSON["features"]:  # procurando chave features 
            if local["properties"]["place"] == "190km ENE of Olonkinbyen, Svalbard and Jan Mayen" :
                print("****Encontrado registro especial*****")
            else:
                print(local["properties"]["place"])

ManipulaJSON()

