def loopBreak():
    for x in range(5,10):
        if x == 7: # verificar se x é giual 7
            break # se x = 7 quero q o loop acabe 
        # comando break interrompe execução de um loop
        print ("O valor de x é: " , x)

#loopBreak()

def loopContinue():
    for x in range(5,10):
        if x == 7: # Não quero q imprime o valor de x = 7
            continue
        print("O valor de x é: ", x)

loopContinue()


