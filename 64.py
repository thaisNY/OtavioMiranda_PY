#Set só suporta elementos unicos, qualquer elem
#Nao dá para criar um set vazio assim s = {}
#SET AND ADD
s1 = {1,2,3,4,5}
print(s1)
s2 = set()
s2.add(1)
s2.add(2)
s2.add(4)
print(s2)
s3 = set()
s3.add('Thais')
s3.add(2)
s3.add((1,22,3,'Thais'))
print(s3)
#add adiciona tuplas e elementos
#A função add não adiciona listas,dict ou outro set
#E só adiciona 1 elemento por vez

###############################################################################################################################################################################

#DISCARD ao passar um elem como parametro elemina esse
s4 = {10,20,30}
s4.discard(20)
print(s4)

#A UPDATE adiciona um elem como add
#So que ao add ele itera tambem ex, vc adiciona python
#Ela ira adicionar cada letra da string
#O set não respeita ordem
#No caso da updade dá p passar lista, dict outro set como iteravel

s5 = set()
s5.update(s4)
print(s5)
s5.update([1,21,31,41])
print(s5)
##########################################################################################################################################################################

   #UNION-une todos os elementos

s1 = {1,2,3,4,5,7}
s2 = {1,2,3,4,5,6}
s3 = s1 | s2
print(s3) #{1, 2, 3, 4, 5, 6}

#INTERSECTION- o que há em comum
s4 = s1 & s2
print(s4) #{1, 2, 3, 4, 5}

#DIFFERENCE- a ordem importa
#exebi os eleme que só estam presentes no set a esquerda
s5 = s1 - s2
print(s5) #{7}

#SIMETRIC DIFERRENCE- Elems que estão nos dois sets mas não estão em ambos

s6 = s1 ^ s2
print(s6) #{6, 7}
##########################################################################################################################################################################

l1 = ['Luiz','João','Maria','Maria']
l2 = ['João','João','João','Maria','Luiz','Luiz']
print(l1 == l2) #False

l1 = set(l1)
l2 = set(l2)
print(l1 == l2) #True

l1 = list(l1) # essa op pode mudar a ordem
l2 = list(l2)
print(l1,l2)

if set(l1) == set(l2): # n muda a ordem,só checa
    print('Sao iguais')
else:
    print('São diferentes')

#Eh possivel fazer typecast para set para descobrir se dois objetos são iguais, sem contar os repetidos
