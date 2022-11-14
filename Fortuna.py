import random
from termcolor import *

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
          'correta': 'D'},

          {'titulo': 'Quantos gols Ronaldo Fenômeno fez oficialmente?',
          'nivel': 'dificil',
          'opcoes': {'A': '815', 'B': '414', 'C': '1100', 'D': '1057'},
          'correta': 'B'},

          {'titulo': 'Quantos metros de altura tem o homem mais alto do mundo?',
          'nivel': 'dificil',
          'opcoes': {'A': '1,54', 'B': '2,51', 'C': '2.42', 'D': '2.36'},
          'correta': 'B'},

          {'titulo': 'Normalmente, quantos litros de sangue uma pessoa tem?',
          'nivel': 'dificil',
          'opcoes': {'A': 'Tem entre 2 a 4 litros.', 'B': 'Tem entre 4 a 6 litros.', 'C': 'Tem 10 litros. ', 'D': 'Tem 7 litros.'},
          'correta': 'B'},

          {'titulo': 'De quem é a famosa frase “Penso, logo existo”?',
          'nivel': 'facil',
          'opcoes': {'A': 'Platão', 'B': 'Galileu Galilei', 'C': 'Descartes', 'D': 'Sócrates'},
          'correta': 'C'},

          {'titulo': 'De onde é a invenção do chuveiro elétrico?',
          'nivel': 'facil',
          'opcoes': {'A': 'Alemanha', 'B': 'Itália', 'C': 'Austrália', 'D': 'Brasil'},
          'correta': 'D'},

          {'titulo': 'Qual o menor país do mundo?',
          'nivel': 'facil',
          'opcoes': {'A': 'Monaco', 'B': 'Vaticano', 'C': 'Nauru', 'D': 'São Marino'},
          'correta': 'B'},

          {'titulo': 'Qual o maior país do mundo?',
          'nivel': 'facil',
          'opcoes': {'A': 'Brasil', 'B': 'China', 'C': 'Russia', 'D': 'Canadá'},
          'correta': 'C'},

          {'titulo': 'Qual o nome do presidente do Brasil que ficou conhecido como Jango?',
          'nivel': 'medio',
          'opcoes': {'A': 'Jânio Quadros', 'B': 'Jacinto Anjos', 'C': 'Getúlio Vargas', 'D': 'João Goulart'},
          'correta': 'D'},

          {'titulo': 'Qual o livro mais vendido no mundo a seguir à Bíblia?',
          'nivel': 'medio',
          'opcoes': {'A': 'O Senhor dos Anéis', 'B': 'Dom Quixote', 'C': 'O Pequeno Príncipe', 'D': 'Um Conto de Duas Cidades'},
          'correta': 'B'},

          {'titulo': 'Quantas casas decimais tem o número pi?',
          'nivel': 'facil',
          'opcoes': {'A': 'Infinitas', 'B': 'Centenas', 'C': 'Dezenas', 'D': 'Milhares'},
          'correta': 'A'},

          {'titulo': 'Atualmente, quantos elementos químicos a tabela periódica possui?',
          'nivel': 'dificil',
          'opcoes': {'A': '113', 'B': '118', 'C': '109', 'D': '98'},
          'correta': 'B'},

          {'titulo': 'O que a palavra legend significa em português?',
          'nivel': 'facil',
          'opcoes': {'A': 'Legenda', 'B': 'Conto', 'C': 'Lenda', 'D': 'Legendário'},
          'correta': 'C'},

          {'titulo': 'Qual o número mínimo de jogadores em cada time numa partida de futebol?',
          'nivel': 'medio',
          'opcoes': {'A': '8', 'B': '10', 'C': '11', 'D': '7'},
          'correta': 'D'},

          {'titulo': 'Quais os principais autores do Barroco no Brasil?',
          'nivel': 'dificil',
          'opcoes': {'A': 'Gregório de Matos, Bento Teixeira e Manuel Botelho de Oliveira', 'B': 'Miguel de Cervantes, Gregório de Matos e Danthe Alighieri', 'C': 'Padre Antônio Vieira, Padre Manuel de Melo e Gregório de Matos', 'D': 'Castro Alves, Bento Teixeira e Manuel Botelho de Oliveira'},
          'correta': 'D'},

          {'titulo': 'Quais as duas datas que são comemoradas em novembro?',
          'nivel': 'facil',
          'opcoes': {'A': 'Independência do Brasil e Dia da Bandeira', 'B': 'Black Friday e Dia da Árvore', 'C': 'Promoção no Burger King e Dia da salsicha', 'D': 'Proclamação da República e Dia Nacional da Consciência Negra'},
          'correta': 'D'},

          {'titulo': 'Quanto tempo a luz do Sol demora para chegar à Terra?',
          'nivel': 'dificil',
          'opcoes': {'A': '12 minutos', 'B': '1 dia', 'C': '8 minutos', 'D': '7 dias'},
          'correta': 'C'},

          {'titulo': 'Quem pintou "Guernica"?',
          'nivel': 'medio',
          'opcoes': {'A': 'Salvador Dalí', 'B': 'Roger Guedes', 'C': 'Pablo Picasso', 'D': 'Rogério Ceni'},
          'correta': 'C'},

          {'titulo': 'Qual a nacionalidade de Che Guevara?',
          'nivel': 'medio',
          'opcoes': {'A': 'Brasileiro', 'B': 'Romeno', 'C': 'Cubano', 'D': 'Argentino'},
          'correta': 'D'},

          {'titulo': 'Qual personagem folclórico costuma ser agradado pelos caçadores com a oferta de fumo?',
          'nivel': 'medio',
          'opcoes': {'A': 'Caipora', 'B': 'Saci', 'C': 'Boitatá', 'D': 'Ian Faray'},
          'correta': 'A'},

          {'titulo': 'Quem é o autor de “O Príncipe”?',
          'nivel': 'medio',
          'opcoes': {'A': 'Maquiavel', 'B': 'Bruno Onishi', 'C': 'Torricelli', 'D': 'Jair Bolsonaro'},
          'correta': 'A'},

          







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
n_quest = 0
acertos = 0
fim = False
sorteio_questao = []
niveis = {
    0: 'facil', 1: 'facil', 2: 'facil',
    3: 'medio', 4: 'medio', 5: 'medio',
    6: 'medio', 
    7: 'dificil', 8: 'dificil', 9: 'dificil'
}

for a in valida_questoes(quest):
    if a != {}:
        fim = True
        cprint("Há questões inválidas", 'red')
        print(valida_questoes(quest))

print("Olá! Você está na Fortuna DeSoft e terá a oportunidade de enriquecer!"'\n')

nome = input("Qual seu nome?")

print('\n'"Ok {0}, você tem direito a pular 3 vezes e 2 ajudas!".format(nome.upper()))
print('As opções de resposta são "A", "B", "C", "D", "ajuda", "pula" e "parar"!''\n')

enter = input("Aperte ENTER para continuar...")

while not fim:
    atual = sorteia_questao_inedita(questoes, niveis[acertos], sorteio_questao)
    n_quest += 1
    fim_quest = False
    precisou_ajuda = False

    while not fim and not fim_quest:
        print(questao_para_texto(atual,n_quest))
        resp = input("Sua resposta: ")

        if resp == atual['correta']:
            acertos += 1
            cprint("VOCÊ ACERTOU! O seu prêmio atual é R$ {:05.2f}".format(lista_premio[acertos]), 'green')
            fim_quest = True
        elif resp == 'pula':
            if pulos == 0:
                cprint('Puts, você não tem mais pulos disponíveis', 'red')
                input('Aperte ENTER para responder novamente...')
            else:
                pulos -= 1
                if pulos == 0:
                    print('Você utilizou seu último pulo!')
                else:
                    cprint("Você pulou a questão e ainda tem {0} pulos disponíveis".format(pulos), 'cyan')
                    fim_quest = True
        elif resp == 'ajuda':
            if ajudas == 0:
                cprint("Deu ruim! Você não tem mais ajudas, vai ter que ser na raça!", 'red')
                input('Aperte ENTER para responder novamente...')
            elif precisou_ajuda:
                cprint("Opa! Você ja usou ajuda nessa questão! Ta tentando roubar?!", 'red')
                input('Aperte ENTER para responder novamente...')
            else:
                ajudas -= 1
                precisou_ajuda = True
                print(gera_ajuda(atual))
                cprint("Você usou uma ajuda e ainda tem {0} ajudas disponíveis".format(ajudas), 'cyan')
        elif resp == 'parar':
            cprint("Você parou com R$ {:05.2f}, vai fazer o que com essa grana?".format(lista_premio[acertos]), 'green')
            fim = True
        elif resp in ['A', 'B', 'C', 'D']:
            cprint('ERRRRRRRROU! Vacilou e perdeu tudo!', 'red')
            fim = True
        else:
            cprint('OPÇÃO INVÁLIDA!', 'red')
            print("As opções de resposta são 'A', 'B', 'C', 'D', 'ajuda', 'pula' ou 'parar'")
            input('Aperte ENTER para responder novamente...')

                



    if acertos == 9: 
        fim = True

    if fim == True:
        jogar_novamente = input("Gostaria de jogar novamente? [Sim/Não]")
        if jogar_novamente.lower() == 'sim':
            fim = False
            ajudas = 2
            pulos = 3
            n_quest = 0
            acertos = 0
            sorteio_questao = []
        else:
            print("Obrigado por jogar!")



