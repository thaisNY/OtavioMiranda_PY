d1 = {'chave1': 'valor da chave'}
#adicioando uma nova chave
d1['nova_chave'] = 'valor da nova chave'
print(d1)
#outra maneira eh usar o construtor dict
d2 = dict(chave1= 'Valor da chave', chave2 = 'valor da outra chave')
print(d2)

#Eh necessario que as chaves sejam unicas, isso não é necessario para os valores

d1 = {
    'str' : 'valor',
    123 : 'outro_valor',
    (1,2,3) : 'trupla',
}

print(d1)
#{'str': 'valor', 123: 'outro_valor', (1, 2, 3): 'trupla'}
#caso você tente acessar uma chave que não existe vai retornar um key error
#para contornar isso é possivel usar o get

d1 = {
    'str' : 'valor',
    123 : 'outro_valor',
    (1,2,3) : 'trupla',
}

if d1.get('nomedachave') is not None:
    print(d1.get('nomedachave'))
    
print(123)

#######################################################################################################################################################################

d1 = {
    'str' : 'valor',
    123 : 'outro_valor',
    (1,2,3) : 'trupla',
}

#Há duas maneiras de alterar o valor de uma chave 
#primeira
d1['str'] = 'novo valor'
#segunda
d1.update({123 : 'novo valor2'})
print(d1)
#{'str': 'novo valor', 123: 'novo valor2', (1, 2, 3): 'trupla'}

#############################################################################################################################################################################

#deletando uma chave

d1 = {
    'str' : 'valor',
    123 : 'outro_valor',
    (1,2,3) : 'trupla',
}

del d1['str']
print(d1)
#{123: 'outro_valor', (1, 2, 3): 'trupla'}
print(str in d1)
#False


print(123 in d1.keys()) #True
print('outro_valor' in d1.values()) #True

#len do dict nos retorna quantos pares existem no dict
print(len(d1)) #2

############################################################################################################################################################################

d2 = {
    'chave1' :'valor1',
    'chave2': 'valor2',
    'chave3': 'valor3',
}

for k in d2:
    print(k)
    
#chave1
#chave2
#chave3

for v in d2.values():
    print(v)
    
#valor1
#valor2
#valor3

for k in d2.items():
    print(k)
    
#('chave1', 'valor1')
#('chave2', 'valor2')
#('chave3', 'valor3')

for k in d2.items(): #for k, v in d2.items():
    print(k[0],k[1]) #print(k,v)
    
#chave1 valor1
#chave2 valor2
#chave3 valor3
##########################################################################################################################################################################

#Percorrendo um dicts dentro de dicts

clientes = {
    'cliente1' : {'nome':'Joao','sobrenome':'Motta'},
    'cliente2' : {'nome':'Thais', 'sobrenome':'Queiroz'}
}

for k,v in clientes.items():
    print(f'Exebindo {k}')
    for dados_k, dados_v in v.items():
        print(f' \t {dados_k} = {dados_v}')
        
#Exebindo cliente1
# 	 nome = Joao
# 	 sobrenome = Motta
#Exebindo cliente2
# 	 nome = Thais
# 	 sobrenome = Queiroz

############################################################################################################################################################################
#Ao salvar um dict em uma variavel voce faz uma copia ou seja ao alterar o dict da variavel o original tambem eh modificado para evitar isso use o copy

d1 = {1:'a',2:'b',3:'c'}
v = d1.copy()
v[1] = 'Thais'
print(d1)
print(v)
#{1: 'a', 2: 'b', 3: 'c'}
#{1: 'Thais', 2: 'b', 3: 'c'}

#O copy usado a maneira acima não é 100% efetivo se o value for uma lista ou outro dict ele ainda vai copiar e modificar o dict original o melhor seria usar o deep copy

import copy
d1 = {1:'a',2:'b',3:'c',4:['Thais','Larissa']}
v =  copy.deepcopy(d1)

v[4][0] = 'Rafaela'
print(d1)
print(v)

#{1: 'a', 2: 'b', 3: 'c', 4: ['Thais', 'Larissa']}
#{1: 'a', 2: 'b', 3: 'c', 4: ['Rafaela', 'Larissa']}

#Inclusive ele consegue modificar até mesmo uma trupla

import copy
d1 = {1:'a',2:'b',3:'c',4:('Thais','Larissa')}
v =  copy.deepcopy(d1)

v[4] = ('Larissa','Thais')
print(d1)
print(v)

#{1: 'a', 2: 'b', 3: 'c', 4: ('Thais', 'Larissa')}
#{1: 'a', 2: 'b', 3: 'c', 4: ('Larissa', 'Thais')}

##########################################################################################################################################################################

#Eh interessante fazer typecast de lista de listas ou truplas de truplas ou lista de truplas ou truplas de listas quando a um par chave e valor a exemplo:

lista = [
    ['c1',1],
    ['c2',2],
    ['c3',3]]
    
d1 = dict(lista)
print(d1)

#{'c1': 1, 'c2': 2, 'c3': 3}

##########################################################################################################################################################################

d1 = {
    1:2,
    3:4,
    5:6
}
d1.pop(3)
print(d1)
#{1: 2, 5: 6}

d1 = {
    1:2,
    3:4,
    5:6
}
d1.popitem()
print(d1)

#{1: 2, 3: 4}- popitem elemina o ultimo, n se passar parametro no popitem()

#concatenando dois dicionarios


d1 = {
    1:2,
    3:4,
    5:6
}
d2 = {
    'a':'b',
    'c':'d',
    'e':'f'
}
d1.update(d2)
print(d1)
#{1: 2, 3: 4, 5: 6, 'a': 'b', 'c': 'd', 'e': 'f'}
