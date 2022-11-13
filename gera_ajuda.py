import random

def gera_ajuda(questao):
    l1 = []
    l2= []

    for a,b in questao['opcoes'].items():
        if a not in questao['correta']:
            l1.append(b)
    
    i = 0
    aleatorio = random.randint(1,2)

    while i < aleatorio:
        incorreta = random.choice(l1)
        l2.append(incorreta)
        l1.remove(incorreta)
        i += 1
    
    if aleatorio == 1:
        return 'DICA:\nOpções certamente erradas: {0}'.format(l2[0])
    else:
        return 'DICA:\nOpções certamente erradas: {0} | {1}'.format(l2[0], l2[1])