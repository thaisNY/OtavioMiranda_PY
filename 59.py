#1 desafio
def ola_mundo():
    return 'Ola Mundo'
    
def mestre(funcao):
    return funcao()

executando = mestre(ola_mundo)
print(executando)

#2 desafio
def mestre(funcao,*args,**kwargs):
    return funcao(*args,**kwargs)
    
def fala_oi(nome):
    return f'Oi {nome}'
    
def saudacao(nome,saudacao):
    return f'{saudacao} {nome}'
    
executando = mestre(fala_oi,'Thais')
print(executando)
