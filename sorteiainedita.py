import random

def sorteia_questao_inedita(dic, nivel, lista):
    t = True
    while t == True:   
        a = random.choice(dic[nivel])
        if a not in lista:
            t = False
            lista.append(a)
    return (a)
    