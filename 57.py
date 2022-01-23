variavel = 'valor'
def func1():
    print(variavel)
def func2():
    variavel = 'Outro valor'
    print(variavel)

print(variavel)
func1()
func2()
#output
#valor
#valor
#Outro valor

#alterando a variavel no escopo da função não altera o seu escopo global caso você queira fazer isso use o global.Mas isso não é uma boa pratica

variavel = 'valor'
def func1():
    print(variavel)
def func2():
    global variavel
    variavel = 'Outro valor'
    print(variavel)

func1()
func2()
print(variavel)

#uma boa pratica eh passar argumentos inves de alterar a variavel global

variavel = 'valor'
def func1():
    print(variavel)
def func2(arg=None):
    arg = arg.replace('v','c')
    return arg

func1()
outra_variavel = func2(arg=variavel)
print(outra_variavel)

#output valor
#calor

#########################################################################################################################################################################
variavel = 'valor'
def func1():
    print(variavel)
    variavel = 1234
    print(variavel)
    
func1()
#erro - chamando uma variavel antes de declarar, o processador vai entender que variavel é a do bloco não a global

#passando variaveis dentro de bloco de uma função para outra função
variavel = 'valor'
def func1():
    outra_variavel = 'Luiz Otavio'
    return outra_variavel
    
def func2(arg):
    print(arg)

var = func1()
func2(var)


