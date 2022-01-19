nome = input('Digite seu nome ')
print(nome or None or 0 or 'Voce nao degitou nada')
#############################################################################################################################################################################
a = 0
b = None
c = False
d = []
e = {}
f = 22
g = 'Thais'
#a b c d e n sao exebidos pq retornam falso
variavel = a or b or c or d or e or f or g
#evita de usar vários ifs
print(variavel)
