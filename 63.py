perguntas = {
    'Pergunta1':{
        'pergunta':'Quanto é 2 + 2?',
        'respostas': {'a':2,'b':22,'c':4},
        'resposta_certa':'c'
    },
    'Pergunta2':{
        'pergunta':'Quanto é 2 - 2?',
        'respostas': {'a':2,'b':0,'c':4},
        'resposta_certa':'b'
    }
}
acertos = 0
for pk,pv in perguntas.items():
    print(f'{pk} {pv["pergunta"]}')
    
    for rk,rv in pv["respostas"].items():
        print(f'{rk} {rv}')
    print()
    resp_user = input('Digite a sua resposta')
    if resp_user == pv["resposta_certa"]:
        print("Voce acertou!!!")
        acertos += 1
    else:
        print("Voce errou!!")

qtd_perguntas = len(perguntas)
porcento = (acertos/qtd_perguntas)*100
print(f'Voce acertou {acertos} perguntas e teve um percentual de {porcento} perguntas acertadas')
        
