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
    