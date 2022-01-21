def saudacao(msg='Ola', nome='Pessoa'):
    nome = nome.replace('e','3')
    msg = msg.replace('e','3')
    print(msg, nome)
    
saudacao() 
saudacao(nome='Zé')
saudacao('Ola','Thais')
saudacao('Hi','Rodrigues')
saudacao('Hello','Queiroz')
#########################################################################################################################################################################

def saudacao(msg='Ola', nome='Pessoa'):
    nome = nome.replace('e','3')
    msg = msg.replace('e','3')
    return f'{msg} {nome}'
    
variavel = saudacao()
print(variavel)
    
