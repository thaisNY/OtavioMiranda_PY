#1 crie uma função que com os parametros saudação e nome
def exebir(saudacao,nome):
    print(saudacao,nome)
exebir('Oi','Thais')
exebir('Ola','Queiroz')

#2 - Crie uma função que recebe três numeros como parametros e exibe a soma deles 
def somaDeTres(a,b,c):
    #print(a + b + c)
    return (a + b + c)

somaDeTres(10,10,10)
somaDeTres(10,20,30)

#3 -Crie uma função que recebe dois números o primeiro um valor e o segundo um percentual,retorne o primeiro somado ao seu respectivo aumento percentual

def calculoDoAumento(valor,percentual):
    aumento = valor + ((valor*percentual)/100)
    #print(aumento)
    return aumento
    
calculoDoAumento(100,10)
calculoDoAumento(200,10)
calculoDoAumento(1000,100)

#4 FizzBuzz Se o parâmetro for divisivel por 2, retorne Fizz.Se o parametro for divisivel por 5 retorna Buzz.Se for divisivel por 5 e por 3 retorna FizzBuzz, caso contrario retorne o numero enviado

def fizzBuzz(num):
    if num % 5 == 0 and num % 3 == 0:
        nome = 'FizzBuzz'
        return nome
    elif num % 5 == 0:
        nome = 'Buzz'
        return nome
    elif num % 3 == 0:
        nome = 'Fizz'
        return nome
    else:
        return num
    
 
print(fizzBuzz(10))
print(fizzBuzz(3))
print(fizzBuzz(30))
print(fizzBuzz(13))



