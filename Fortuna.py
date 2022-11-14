import random

quest = [{'titulo': 'Qual o resultado da operação 57 + 32?',
          'nivel': 'facil',
          'opcoes': {'A': '-19', 'B': '85', 'C': '89', 'D': '99'},
          'correta': 'C'},

         {'titulo': 'Qual a capital do Brasil?',
          'nivel': 'facil',
          'opcoes': {'A': 'Brasília', 'B': 'Rio de janeiro', 'C': 'São Paulo', 'D': 'Osasco'},
          'correta': 'A'},

         {'titulo': 'Quando é o feriado da Independência do Brasil?',
          'nivel': 'facil',
          'opcoes': {'A': '21 de Abril', 'B': '12 de Outubro', 'C': '07 de Setembro', 'D': '15 de Novembro'},
          'correta': 'C'},

         {'titulo': '_________ é um conjunto de particularidades que caracterizam um grupo de pessoas, uma família ou uma sociedade. É formada por princípios morais, hábitos, costumes, histórias, manifestações religiosas, entre outros. Qual palavra melhor completa o início da frase?',
          'nivel': 'facil',
          'opcoes': {'A': 'Missão', 'B': 'Cultura', 'C': 'Curso superior', 'D': 'Culinária'},
          'correta': 'B'},

         {'titulo': 'Qual destes termos menos tem relação com o fenômeno da globalização?',
          'nivel': 'facil',
          'opcoes': {'A': 'Aculturação', 'B': 'Neoliberalismo', 'C': 'União Europeia', 'D': 'Caldeirão do Huck'},
          'correta': 'D'},

         {'titulo': 'Qual o feriado do aniversário da cidade de São Paulo?',
          'nivel': 'facil',
          'opcoes': {'A': '25 de Janeiro', 'B': '24 de Março', 'C': '9 de Julho', 'D': '12 de Novembro'},
          'correta': 'A'},

         {'titulo': 'Qual destas não é uma fruta?',
          'nivel': 'facil',
          'opcoes': {'A': 'Laranja', 'B': 'Maça', 'C': 'Tomate', 'D': 'Abacate'},
          'correta': 'B'},

         {'titulo': 'Em qual ano o TikTok atingiu 1 bilhão de usuários?',
          'nivel': 'facil',
          'opcoes': {'A': '2019', 'B': '2021', 'C': '2015', 'D': '2018'},
          'correta': 'B'},
         
         {'titulo': 'Qual destes não é um app com foco em streaming de vídeo?',
          'nivel': 'facil',
          'opcoes': {'A': 'Netflix', 'B': 'Disney Plus', 'C': 'TIDAL', 'D': 'HBO Max'},
          'correta': 'C'},

         {'titulo': 'Qual destes parques não se localiza em São Paulo?!',
          'nivel': 'facil',
          'opcoes': {'A': 'Ibirapuera', 'B': 'Parque do Carmo', 'C': 'Parque Villa Lobos', 'D': 'Morro da Urca'},
          'correta': 'D'},

         {'titulo': 'Qual destas não é uma linguagem de programação?',
          'nivel': 'facil',
          'opcoes': {'A': 'Miratdes', 'B': 'Python', 'C': 'Lua', 'D': 'C++'},
          'correta': 'A'},

         {'titulo': 'Dentre os listados, qual destes esportes é menos praticado no Brasil?',
          'nivel': 'facil',
          'opcoes': {'A': 'Natação', 'B': 'Vôlei', 'C': 'Ski Cross Country', 'D': 'Futebol'},
          'correta': 'C'},
         
         {'titulo': 'Qual o resultado da operação 5 + 2 * 3?',
          'nivel': 'medio',
          'opcoes': {'A': '21', 'B': '11', 'C': '30', 'D': '10'},
          'correta': 'B'},

         {'titulo': 'Qual destas é uma pseudociência que estuda os corpos celestes e as prováveis relações que possuem com a vida das pessoas e os acontecimentos na Terra?',
          'nivel': 'medio',
          'opcoes': {'A': 'Astronomia', 'B': 'Física quântica', 'C': 'Astrologia', 'D': 'Computação'},
          'correta': 'C'},

         {'titulo': 'Qual destas não foi considerada em 2007 uma das sete maravilhas do mundo moderno?',
          'nivel': 'medio',
          'opcoes': {'A': 'Muralha da China', 'B': 'Machu Picchu', 'C': 'Cristo Redentor', 'D': 'Torre Eiffel'},
          'correta': 'D'},

         {'titulo': 'Qual destas pessoas conduziu importantes estudos sobre radioatividade, sendo ganhadora de dois prêmios Nobel?',
          'nivel': 'medio',
          'opcoes': {'A': 'Marie Curie', 'B': 'Paul Erdős', 'C': 'Clive W.J. Granger', 'D': 'Maria Ressa'},
          'correta': 'A'},

         {'titulo': 'Quem é considerada a primeira pessoa programadora do mundo?!',
          'nivel': 'medio',
          'opcoes': {'A': 'Marie Curie', 'B': 'Alan Turing', 'C': 'Ada Lovelace', 'D': 'Edsger Dijkstra'},
          'correta': 'C'},

         {'titulo': 'Qual destes números é primo?',
          'nivel': 'medio',
          'opcoes': {'A': '259', 'B': '85', 'C': '49', 'D': '19'},
          'correta': 'D'},

         {'titulo': 'Na Conjectura de _______, escolhendo-se um número natural inicial n, onde n > 0, os seguintes critérios serão obedecidos: Se n for par o seu sucessor será a metade e se n for ímpar o seu sucessor será o triplo mais um, gerando então um novo número. Qual o nome da conjectura?',
          'nivel': 'medio',
          'opcoes': {'A': 'Collatz', 'B': 'Goldbach', 'C': 'Poincaré', 'D': 'Hodge'},
          'correta': 'A'},

         {'titulo': 'Como faço para chamar o SAMU?',
          'nivel': 'medio',
          'opcoes': {'A': 'Ligue 101', 'B': 'Ligue 192', 'C': 'Ligue 109', 'D': 'Ligue 122'},
          'correta': 'B'},

         {'titulo': 'Qual a segunda pessoa mais seguida no Instagram?',
          'nivel': 'medio',
          'opcoes': {'A': 'Cristiano Ronaldo', 'B': 'Dwayne Johnson', 'C': 'Kim Kardashian', 'D': 'Kylie Jenner'},
          'correta': 'D'},

         {'titulo': 'Qual a pessoa mais seguida no Instagram?',
          'nivel': 'medio',
          'opcoes': {'A': 'Cristiano Ronaldo', 'B': 'Dwayne Johnson', 'C': 'Kim Kardashian', 'D': 'Lionel Messi'},
          'correta': 'A'},

         {'titulo': 'A reprodução dos seres vivos é um processo biológico através do qual os organismos geram descendência. Qual desta não é uma forma de reprodução assexuada?',
          'nivel': 'dificil',
          'opcoes': {'A': 'Autogamia', 'B': 'Esporulação', 'C': 'Partenogênese', 'D': 'Divisão binária'},
          'correta': 'A'},

         {'titulo': 'Qual o resultado da operação 5 + 2 * 3 ^ 2, onde ^ representa potenciação?',
          'nivel': 'dificil',
          'opcoes': {'A': '441', 'B': '86', 'C': 'Nenhuma das outras respostas', 'D': '23'},
          'correta': 'D'},

         {'titulo': 'Quem é Oxóssi?!',
          'nivel': 'dificil',
          'opcoes': {'A': 'Rede de mercados', 'B': 'Tipo de poema Dissílabo', 'C': 'Divindade das religiões africanas', 'D': 'Trapper brasileiro'},
          'correta': 'C'},

         {'titulo': 'Qual a altura do Cristo Redentor?',
          'nivel': 'dificil',
          'opcoes': {'A': 'entre 0 e 20 metros', 'B': 'Entre 21 e 40 metros', 'C': 'Entre 41 e 60 metros', 'D': 'Mais que 60 metros'},
          'correta': 'B'},

         {'titulo': 'Em que ano faleceu Charles Babbage?',
          'nivel': 'dificil',
          'opcoes': {'A': '2022', 'B': '1791', 'C': '1935', 'D': '1871'},
          'correta': 'A'},

         {'titulo': 'Einstein foi Nobel de física em qual ano?',
          'nivel': 'dificil',
          'opcoes': {'A': '1906', 'B': '1905', 'C': '1920', 'D': '1921'},
          'correta': 'D'},

         {'titulo': 'Qual o número atômico do nitrogênio?',
          'nivel': 'dificil',
          'opcoes': {'A': '9', 'B': '7', 'C': '6', 'D': '8'},
          'correta': 'B'},

         {'titulo': 'Qual o ponto de fusão do nitrogênio?',
          'nivel': 'dificil',
          'opcoes': {'A': '120º C', 'B': '15º C', 'C': '-210º C', 'D': '-180º C'},
          'correta': 'C'},
         
         {'titulo': 'Quantos gols Pelé fez oficialmente?',
          'nivel': 'dificil',
          'opcoes': {'A': '815', 'B': '762', 'C': '1100', 'D': '1057'},
          'correta': 'B'},

         {'titulo': 'O que é Necrose?',
          'nivel': 'dificil',
          'opcoes': {'A': 'Uma banda de Rock', 'B': 'Uma marca de luxo', 'C': 'Cidade Francesa', 'D': 'Morte de tecido orgânico'},
          'correta': 'D'}
        ]


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
