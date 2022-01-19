#minha resolução do desafio cpf - validador de cpf


cpf = input('Digite o seu cpf ')
cpf_num = []
for i in range(len(cpf)):
    if cpf[i].isnumeric():
        cpf_num.append(cpf[i])
        
cpf_num.pop()
cpf_num.pop()

count = 11
sum = 0
for j in range(len(cpf_num)):
    count = count - 1
    valor = int(cpf_num[j]) * int(count)
    print(f'{cpf_num[j]} x {count} = {valor} ')
    sum += valor
    
print(sum)
res = 11 - (sum % 11)
print(res)
if res > 9:
    dig1 = 0
else:
    print('cpf invalido')
    
count2 = 12
sum2 = 0
valor2 = 0

for k in range(len(cpf_num)):
    count2 = count2 - 1
    valor2 = int(cpf_num[k]) * int(count2)
    print(f'{cpf_num[k]} x {count2} = {valor2} ')
    sum2 += valor2
print(sum2)
sum2 += dig1 * 2
print(sum2)
res2 = 11 - (sum2 % 11)
print(res2)
if res2 <= 9:
    dig2 = 9
else:
    print('cpf invalido')

novo_cpf = ''  
for l in range(len(cpf_num)):
    novo_cpf += cpf_num[l]
novo_cpf += (str(dig1) + str(dig2))
print(novo_cpf)
