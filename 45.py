logged_user = True
if logged_user:
    msg = 'Usuario logado.'
else:
    msg = 'Usuario precisa logar.'
    
print(msg)
#########################################################################################################################################################################
#Mesmo código com ternário

logged_user = True
msg = 'Usuario logado' if logged_user else 'Usuario precisa logar'
    
print(msg)
###########################################################################################################################################################################
 idade = input('Digite a idade')

if not idade.isnumeric():
    print('voce precisa digitar apenas números')
else:
    idade = int(idade)
    maior_idade = (idade >= 18)
    msg = 'Pode logar' if maior_idade else 'Nao pode logar'
    
    print(msg)
