# print ("Hello World") 

# Trabalhando com variáveis 
f=0
print(f)

f= "abc"
print(f)

print("isso é uma string" + str(123))

def AlgumaFuncao ():
    global f
    f= "def"
    print(f)

AlgumaFuncao() 
print(f)