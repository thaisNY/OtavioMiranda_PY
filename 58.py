#extra
def func1():
    valores = [10,20,20]
    return valores
var = func1()
def func2(var):
    n1,n2,n3 = var
    soma = n1 + n2 + n3
    return soma
    
var2 = func2(var)
print(var2)

#1  desafio
def func1():
    valores = [10,20,20]
    return valores
var = func1()
def func2(var):
   
    return var
    
var2 = func2(var)
print(var2)

#2 desafio
def funcao1():
    valores = [10,20,20]
    return valores
var = funcao1()

def funcao2():
    valores = [30,30]
    return valores
var2 = funcao2()

def funcao3(var,var2):
    return var + var2
    
var3 = funcao3(var,var2)
print(var3)



