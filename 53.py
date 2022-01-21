def funcao(var):
    print(var)
    
variavel = funcao('Valor que eu quero')
print(variavel)

#Quando uma função não tem return em py ela irá retornar None
#None é um obj - não valor - tipo de dado

if variavel: #None entra aqui como falso
    print(variavel)
else:
    print('Nenhum valor')
    
#########################################################################################################################################################################

def funcao(var):
   return var
    
variavel = funcao('Valor que eu quero')
print(variavel)

#Quando uma função não tem return em py ela irá retornar None
#None é um obj - não valor - tipo de dado
#Nesse caso sera true e saida será Nenhum valor 
if variavel: 
    print(variavel)
else:
    print('Nenhum valor')
###########################################################################################################################################################################

def divisao(n1,n2):
    if n2 == 0:
        return
    
    return n1/n2
divide = divisao(8,0)
if divide:
    print(divide)
else:
    print('Conta Inválida')
###########################################################################################################################################################################

def dumb():
    return 1.1
print(dumb(),type(dumb()))

#########################################################################################################################################################################
def dumb():
    return [1,2,3] #True retornaria boolean
var = dumb()
print(var,type(var))

#######################################################################################################################################################################

def f(var):
    print(var)

def dumb():
    return f
    
var = dumb()('E colocar meu valor aqui')
var1 = dumb()
print(type(f))
print(type(var1))
print(type(var))
print(id(var1),id(f))

if var1 == f:
    print('Var eh igual a f')
else:
    print('Nao eh igual')
    
#eh o mesmo obj na memoria do computador

#########################################################################################################################################################################

def dumb():
    return 'Luiz','Otavio'

print(dumb())
var = dumb()
print(type(var))
