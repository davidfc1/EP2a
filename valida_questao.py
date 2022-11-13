def valida_questao(dic):
    res = {}
    titulo = True
    nivel = True
    opcoes = True
    correta = True

    if "titulo" not in dic:
        res["titulo"]= "nao_encontrado"
        titulo = False
    if "nivel" not in dic:
        res["nivel"]= "nao_encontrado"
        nivel = False
    if "opcoes" not in dic:
        res["opcoes"]= "nao_encontrado"
        opcoes = False
    if "correta" not in dic:
        res["correta"]= "nao_encontrado"
        correta = False
    
    if len(dic) != 4:
        res['outro'] = 'numero_chaves_invalido'
    
    if titulo == True:
        if len(dic['titulo']) == 0 or dic['titulo'].isspace() == True:
            res['titulo'] = 'vazio'
    if nivel == True:
        if dic['nivel'] != 'facil' and dic['nivel'] != 'medio' and dic['nivel'] != 'dificil':
            res['nivel'] = 'valor_errado'
    if opcoes == True:
        if len(dic['opcoes']) != 4:
            res['opcoes'] = 'tamanho_invalido'
    if correta == True:
        if dic['correta'] != 'A' and dic['correta'] != 'B' and dic['correta'] != 'C' and dic['correta'] != 'D':
            res['correta'] = 'valor_errado'
    
    if opcoes == True and len(dic['opcoes']) == 4 and 'A' not in dic['opcoes'] or 'B' not in dic['opcoes'] or 'C' not in dic['opcoes'] or 'D' not in dic['opcoes']:
        if 'opcoes' not in res:
            res['opcoes'] = 'chave_invalida_ou_nao_encontrad'
    
    if opcoes == True and "A" in dic['opcoes'] and dic['opcoes']['A'].isspace() == True and len(dic['opcoes']) == 4:
        if 'opcoes' not in res:
            res['opcoes'] = {}
            res['opcoes']['A'] = 'vazia'
    if opcoes == True and "B" in dic['opcoes'] and dic['opcoes']['B'].isspace() == True and len(dic['opcoes']) == 4:
        if 'opcoes' not in res:
            res['opcoes'] = {}
            res['opcoes']['B'] = 'vazia'
        else:
            res['opcoes']['B'] = 'vazia'
    if opcoes == True and "C" in dic['opcoes'] and dic['opcoes']['C'].isspace() == True and len(dic['opcoes']) == 4:
        if 'opcoes' not in res:
            res['opcoes'] = {}
            res['opcoes']['C'] = 'vazia'
        else:
            res['opcoes']['C'] = 'vazia'
    if opcoes == True and "D" in dic['opcoes'] and dic['opcoes']['D'].isspace() == True and len(dic['opcoes']) == 4:
        if 'opcoes' not in res:
            res['opcoes'] = {}
            res['opcoes']['D'] = 'vazia'
        else:
            res['opcoes']['D'] = 'vazia'
    
    return res
            
        
                
        
        
        
            
        
    
    

    