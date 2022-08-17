
import calendar # importar módulo calendário

def ImprimeMes (): # função imprime mês 
    for mes in calendar.month_name:  # fazendo loop dentro do objeto que retorna os meses do ano 
        print (mes)

    for dia in calendar.day_name:  # fazendo loop dentro do objeto que retorna os dias  da semana 
        print (dia)
        
ImprimeMes()