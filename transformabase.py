def transforma_base(questoes):
    res = {}
    for a in questoes:
        if a['nivel'] not in res:
            res[a['nivel']] = [a]
        else:
          res[a['nivel']].append(a)  
    
    return res