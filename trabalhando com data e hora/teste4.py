from datetime import date
from datetime import time
from datetime import datetime
from datetime import timedelta  # timedelta --> período de tempo / utilizar essa classe para operações com data
# a classe timedelta é uma das possibilidades de manipulação de datas  
def deltaTempo():  # função delta tempo 
    delta = timedelta(days = 86, hours = 8532, minutes = 7645)  # criando objeto delta 
    # paramentro delta --> dias , horas e minuitos 
    print(delta)

    hoje = datetime.now() # variável hj 
    print("Data no futuro: " , hoje + delta)  # somar delta com o dia de hj 
    print("Data no passado: ", hoje - delta) # resultado da subtração do delta - data hj 

deltaTempo()