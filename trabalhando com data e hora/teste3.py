from datetime import datetime

def FormataDataHora(): # criando uma função 



    hoje = datetime.now()  # criando variável hj 

    print (hoje.strftime("O ano é: %Y"))  # função strftime para formatar data e hora  / pode ser y(22) ou Y (2022) 
    # Possível Formatação --> %y/%Y - Ano, %a/%A - Dia da semana, %b/%B - Mês, %d - dia do mÊs

    print (hoje.strftime("Data e hora local: %c"))  # parametro %c --> para data e hora local atual 
    # Possível Formatação --> %I/%H - 12/24 hpras, %M - minuto, %S - segundo, %p -  AM/PM
  


    print (hoje.strftime("A hora atual é: %I:%M:%S %p"))
    
FormataDataHora()