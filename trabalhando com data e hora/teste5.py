from datetime import date
from datetime import time
from datetime import datetime
from datetime import timedelta

def QuantosDiasFaltam(ano, mes, dia):  # função com 3 parametros 
    hoje = date.today() # variavel com a data de hoje 
    dataProcurada = date(ano, mes, dia)  # criar um objeto com a data procurada
    # obejeto do tipo date 

    qtosDias = dataProcurada - hoje # criando variável para saber quantos dias faltam

    mensagemRetorno = "Faltam " + str(qtosDias).replace("days, 0:00:00", "") + " dias para a data " + dataProcurada.strftime("%d/%m/%y")
  # criando uma mensagem de retorno / concatenar uma msg de string  / str converte objeto em uma string  / concatenar com a data procurada
    # trftime("%d/%m/%y") formatação que queremos na data 
    # função replace para deixar o resultado mais amigável aos olhos kkkkkkk
    print(mensagemRetorno)

QuantosDiasFaltam (2019, 10, 29)