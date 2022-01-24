def funcao(arg1,arg2):
    return arg1 * arg2
var = funcao(2,2)
print(var)
# a função lambda faz a mesma coisa da função acima
a = lambda x,y : x*y
print(a(2,2))


#criando uma função para ordernar uma lista dentro de uma lista
lista = [['P1',12],
         ['P2',21],
         ['P3',2],
         ['P4',100],
         ['P5',121]]
         
def func(item):
    return item[1]
    
lista.sort(key = func, reverse = True)
print(lista)
    
#usando o lambda 
lista = [['P1',12],
         ['P2',21],
         ['P3',2],
         ['P4',100],
         ['P5',121]]

lista.sort(key = lambda item: item[1], reverse = True)
print(lista)
#nao altera a lista original, lambdas funções anonimas
    
