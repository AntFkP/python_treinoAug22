import calendar  # importar módulo caledário 

# parte 1 
def CalendarioTexto(): # função criando um calendário no formato texto
    calendarioTexto = calendar.TextCalendar(calendar.SUNDAY) # objeto calendário texto 
    txtCalendario = calendarioTexto.formatmonth(2019, 6)  # string com o formato do calendário 
    # nesse caso calendário mensal do ano de 2019 do mês 6 
    print (txtCalendario)

 #CalendarioTexto()

def CalendarioHTML():  # função Criando um calendário no formato HTML
    calendarioHTML = calendar.HTMLCalendar(calendar.SUNDAY)
    htmlCalendario = calendarioHTML.formatmonth(2019, 6)
    print (htmlCalendario)

CalendarioHTML()