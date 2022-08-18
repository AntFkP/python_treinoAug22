def loopFor():
    for x in range (5,10):
        print(x)

loopFor()

def loopArray ():
    dias = ["seg", "ter", "qua", "qui", "sex", "sab", "dom"]
    for d in dias:
        print (d)

loopArray()

# Usando a função enumerate, paara buscar valores e seus índices
def loopEnum ():
    dias = ["seg", "ter", "qua", "qui", "sex", "sab", "dom"]
    for i, d in enumerate(dias):
        print (i, d)

loopEnum()
 