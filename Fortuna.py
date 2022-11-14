import random
from questoes import *


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

def questao_para_texto(dic, ID):
    return("----------------------------------------"
    '\n'
    'QUESTAO {0}'
    '\n'
    '\n'
    '{1}'
    '\n'
    '\n'
    'RESPOSTAS:'
    '\n'
    'A: {2}'
    '\n'
    'B: {3}'
    '\n'
    'C: {4}'
    '\n'
    'D: {5}'
    ).format(ID, dic['titulo'], dic['opcoes']['A'], dic['opcoes']['B'], dic['opcoes']['C'], dic['opcoes']['D'])

def sorteia_questao_inedita(dic, nivel, lista):
    t = True
    while t == True:   
        a = random.choice(dic[nivel])
        if a not in lista:
            t = False
            lista.append(a)
    return (a)

def sorteia_questao(dicionario, nivel):
    x = random.choice(dicionario[nivel])
    return x

def transforma_base(questoes):
    res = {}
    for a in questoes:
        if a['nivel'] not in res:
            res[a['nivel']] = [a]
        else:
          res[a['nivel']].append(a)  
    
    return res

def valida_questoes(lista):
    final = []
    for dic in lista:
        res={}

        titulo = True
        nivel = True
        opcoes = True
        correta = True

        if "titulo" not in dic:
            res["titulo"]= "nao_encontrado"
            titulo= False
        if "nivel" not in dic:
            res["nivel"]= "nao_encontrado"
            nivel= False
        if "opcoes" not in dic:
            res["opcoes"]= "nao_encontrado"
            opcoes= False
        if "correta" not in dic:
            res["correta"]= "nao_encontrado"
            correta= False
        if len(dic)!= 4:
            res["outro"]= "numero_chaves_invalido"
        if titulo == True:
            if len(dic["titulo"])== 0 or dic["titulo"].isspace()== True:
                res["titulo"]= 'vazio'
        if nivel == True:
            if dic["nivel"]!= "facil" and dic["nivel"]!= "medio" and dic["nivel"]!= "dificil":
                res['nivel']= 'valor_errado'    
        if opcoes== True: 
            if len(dic["opcoes"])!= 4   :
                res["opcoes"]='tamanho_invalido'
        if opcoes== True: 
            if len(dic["opcoes"])== 4 and "A" not in dic["opcoes"] or "B" not in dic["opcoes"] or "C" not in dic["opcoes"] or "D" not in dic["opcoes"] :
                if 'opcoes'not in res:
                    res['opcoes']='chave_invalida_ou_nao_encontrada'
        
        if opcoes == True and "A"  in dic["opcoes"] and len(dic["opcoes"])== 4 and  dic["opcoes"]['A'].isspace() == True :
            if 'opcoes'not in res:
                res["opcoes"]= {}
                res["opcoes"]["A"]='vazia'  
        if opcoes == True and "B"  in dic["opcoes"] and len(dic["opcoes"])== 4 and  dic["opcoes"]['B'].isspace() == True :
            if 'opcoes'not in res:
                res["opcoes"]= {}
                res["opcoes"]["B"]='vazia'
            else:
                res["opcoes"]["B"]='vazia'
        if opcoes== True and "C"  in dic["opcoes"] and len(dic["opcoes"])== 4 and  dic["opcoes"]['C'].isspace() == True :
            if 'opcoes'not in res:
                res["opcoes"]= {}
                res["opcoes"]["C"]='vazia'
            else:
                res["opcoes"]["C"]='vazia'
        if opcoes== True and "D"  in dic["opcoes"] and len(dic["opcoes"])== 4 and  dic["opcoes"]['D'].isspace() == True :
            if 'opcoes'not in res:
                res["opcoes"]= {}
                res["opcoes"]["D"]='vazia'
            else:
                res["opcoes"]["D"]='vazia'

        
        if correta == True and dic['correta']!= 'A' and dic['correta']!= 'B' and dic['correta']!= 'C'  and dic['correta']!= 'D':
            res['correta']= 'valor_errado'
        
        final.append(res)
    
    return final
    
def valida_questao(dic):
    res={}

    titulo = True
    nivel = True
    opcoes = True
    correta = True

    if "titulo" not in dic:
        res["titulo"]= "nao_encontrado"
        titulo= False
    if "nivel" not in dic:
        res["nivel"]= "nao_encontrado"
        nivel= False
    if "opcoes" not in dic:
        res["opcoes"]= "nao_encontrado"
        opcoes= False
    if "correta" not in dic:
        res["correta"]= "nao_encontrado"
        correta= False
    if len(dic)!= 4:
        res["outro"]= "numero_chaves_invalido"
    if titulo == True:
        if len(dic["titulo"])== 0 or dic["titulo"].isspace()== True:
            res["titulo"]= 'vazio'
    if nivel == True:
        if dic["nivel"]!= "facil" and dic["nivel"]!= "medio" and dic["nivel"]!= "dificil":
            res['nivel']= 'valor_errado'    
    if opcoes== True: 
        if len(dic["opcoes"])!= 4   :
            res["opcoes"]='tamanho_invalido'
    if opcoes== True: 
        if len(dic["opcoes"])== 4 and "A" not in dic["opcoes"] or "B" not in dic["opcoes"] or "C" not in dic["opcoes"] or "D" not in dic["opcoes"] :
            if 'opcoes'not in res:
                res['opcoes']='chave_invalida_ou_nao_encontrada'
    
    if opcoes == True and "A"  in dic["opcoes"] and len(dic["opcoes"])== 4 and  dic["opcoes"]['A'].isspace() == True :
        if 'opcoes'not in res:
            res["opcoes"]= {}
            res["opcoes"]["A"]='vazia'  
    if opcoes == True and "B"  in dic["opcoes"] and len(dic["opcoes"])== 4 and  dic["opcoes"]['B'].isspace() == True :
        if 'opcoes'not in res:
            res["opcoes"]= {}
            res["opcoes"]["B"]='vazia'
        else:
            res["opcoes"]["B"]='vazia'
    if opcoes== True and "C"  in dic["opcoes"] and len(dic["opcoes"])== 4 and  dic["opcoes"]['C'].isspace() == True :
        if 'opcoes'not in res:
            res["opcoes"]= {}
            res["opcoes"]["C"]='vazia'
        else:
            res["opcoes"]["C"]='vazia'
    if opcoes== True and "D"  in dic["opcoes"] and len(dic["opcoes"])== 4 and  dic["opcoes"]['D'].isspace() == True :
        if 'opcoes'not in res:
            res["opcoes"]= {}
            res["opcoes"]["D"]='vazia'
        else:
            res["opcoes"]["D"]='vazia'

    
    if correta == True and dic['correta']!= 'A' and dic['correta']!= 'B' and dic['correta']!= 'C'  and dic['correta']!= 'D':
        res['correta']= 'valor_errado'


    return res

lista_premio = [0.00,1000.00,5000.00,10000.00,30000.00,50000.00,100000.00,300000.00,500000.00,1000000.00]
pulos = 3
ajudas = 2
questoes = transforma_base(quest)