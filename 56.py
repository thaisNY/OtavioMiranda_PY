#obs1
#toda a vez que eu setar um padrão para um argumento tdos dps dele
#precisam ter um valor padrão também

#obs2 
#toda vez que eu chamar uma função e passar como parametro um obj 
#nomeado todos os posteriores precisam ser nomeados tbm 

def func(a1,a2,a3,a4,a5, nome=None, a6=None):
    print(a1,a2,a3,a4,a5,nome,a6)
    return nome,a6
    
var = func(1,2,3,4,5, nome='Luiz',a6='5')

######################################################################################################################################################################
#As vezes acontece de voce não saber quantos elementos vao ser 
#repassados para a função.No caso se usa *args

def func(*args):
    print(args)
    
var = func()

#output ()


lista = [1,2,3,4,5]
n1, n2, *n = lista
print(n1, n2, n)
#output 1 2 [3, 4, 5]

#exebi a lista desempacotada
lista = [1,2,3,4,5]
print(*lista)

#output 1 2 3 4 5

lista = [1,2,3,4,5]
print(*lista,sep='-')

#output 1-2-3-4

#####################################################################################################################################################################

def func(*args):
    print(args)
    print(args[0])
    print(args[-1])
    print(len(args))
    
func(1,2,3,4,5)
    
#output
#(1, 2, 3, 4, 5)
#1
#5
#5

#####################################################################################################################################################################

#typecast de tuplas para lista
def func(*args):
    args = list(args)
    args[0] = 20
    print(args)
    
func(1,2,3,4,5)
#output [20, 2, 3, 4, 5]

########################################################################################################################################################################

#resolvendo a questão de tuplas e listas como mesma saida
def func(*args):
    print(args)
    
lista = [1,2,3,4,5]
func(lista,'6')
#output ([1, 2, 3, 4, 5], '6')

def func(*args):
    print(args)
 #basta desempacotar a lista   
lista = [1,2,3,4,5]
func(*lista,10,20,30,40,50)

#########################################################################################################################################################################

#Mesclando duas listas

def func(*args):
    print(args)
 
lista1 = [1,2,3,4,5]
lista2 = [10,20,30,40,50]
func(*lista1,*lista2)
#output (1, 2, 3, 4, 5, 10, 20, 30, 40, 50)

############################################################################################################################################################################

#kwargs args of keys, argumentos nomeados 
def func(*args,**kwargs):
    print(args)
    print(kwargs)
     print(kwargs['nome'],kwargs['sobrenome'])
 
lista1 = [1,2,3,4,5]
func(*lista1,nome='Thais',sobrenome='Queiroz')

#(1, 2, 3, 4, 5)
#{'nome': 'Thais', 'sobrenome': 'Queiroz'}
#Thais Queiroz

##############################################################################################################################################################################

#usando get para acesar as keys
#exebi o none caso nao exista
def func(*args,**kwargs):
    print(args)
    idade = kwargs.get('idade')
    if idade is not None:
        print(idade)
    
lista1 = [1,2,3,4,5]
func(*lista1,nome='Thais',sobrenome='Queiroz',idade='19')
#caso idade n existisse e eu chamasse como kwargs['idade'] daria erro
#por isso eh melhor usar get

