from datetime import date 
from datetime import time
from datetime import datetime

def mDataHora(): # manipula data e hora 
    hoje = date.today()
    print("Hj é :" , hoje)
    print("Partes da data:" , hoje.day , hoje.month, hoje.year )
    print("Número do dia da semana:", hoje.weekday()) # método weekday que vai retornar qual o dia de hj 
    dias = ["seg", "ter", "qua", "qui", "sex", "sab", "dom"] # criando um array 
    print("Nome abreviado do dia da semana: ", dias[hoje.weekday()]) # weekday para localizar o dia de hj 

    data = datetime.now()   # classe datetime para verificar dia de hj / now--> no dia de hj
    print ("Data e hora: ", data)

    tempo = datetime.time(data)  # variavel tempo para saber a hora atual / parametro variável data 
    print ("Hora atual: ", tempo)
mDataHora()
