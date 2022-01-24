t1 = 1,
print(type(t1))
t2 = 1, 2, 3
print(t2)
#<class 'tuple'>
#(1, 2, 3)

#truplas sao iteraveis e fatiaveis


t3 = 1,2, 'Thais', 4, 5
t4 = 6, 7, 8, 9, 10
t5 = t3 + t4
print(t5)
#(1, 2, 'Thais', 4, 5, 6, 7, 8, 9, 10)

n1,n2,n3,n4,*n_outros,n10 = t5
print(n1, n2, n3,n4)
print(*n_outros)
print(n10)

#1 2 Thais 4
#5 6 7 8 9
#10


n1 = 'oi',
print(n1*10)
#('oi', 'oi', 'oi', 'oi', 'oi', 'oi', 'oi', 'oi', 'oi', 'oi')


t6 = (1,2,3,4)
t6 = list(t6)
t6[2] = 300
t6 = tuple(t6)
print(t6)
#(1, 2, 300, 4)
