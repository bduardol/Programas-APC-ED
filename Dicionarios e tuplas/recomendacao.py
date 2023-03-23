from collections import Counter
import operator
listaf=[]
prin=[]
final=[]
kk={}
f=[]
j=[]
def recomenda(n):
    listaf=[]
    prin=[]
    final=[]
    kk={}
    f=[]
    j=[]
    for i in n:
        for j in i:
            listaf.append(j)
    c= Counter(listaf)

    for i in listaf:
        if i not in f:
            f.append(i)
    for i in f:
        b = c[i]
        kk[i] = b
    j=kk.items()
    j = sorted(j, key= lambda t: t[1], reverse=True)
    
    x=j[0][1]    
    
    for i in j:
        if i[1] == x and i not in final:
            final.append(i[0])
    return final
        
            
    
tags = [['lançamento', 'palavra', 'malhação', 'veteranos', 'comida', 'lista', 'academia', 'famosos', 'you'], ['cachorro', 'educação', 'parkour', 'lançamento', 'programação', 'covid'], ['bom', 'golpe', 'frio', 'trendy', 'questão', 'gameplay', 'destino', 'aulas', 'comida', 'lasanha'], ['fofoca', 'parkour', 'MC', 'comédia', 'Ruby', 'aulas', 'comida', 'deus', 'a', 'tutorial'], ['educação', 'matriz', 'questão', 'head', 'famosos', 'programação', 'lasanha'], ['funk'], ['gato', 'EAD'], ['roupas', 'funk', 'ação', 'Ruby', 'lista'], ['cachorro', 'restauração', 'Ruby', 'calouros', 'famosos', 'you'], ['pop', 'body', 'JavaScript', 'ação', 'tiktok', 'Ruby', 'destino', 'opções'], ['esportes', 'funk', 'quarentena', 'font', 'babados', 'batata'], ['signos', 'quarentena', 'veteranos', 'batata', 'filmes'], ['EAD'], ['roupas', 'lançamento', 'EAD'], ['golpe', 'fogo', 'ação', 'aulas', 'opções'], ['cachorro', 'místico', 'drama', 'fashion', 'a', 'lasanha'], ['esportes', 'funk', 'Java', 'academia', 'beijei', 'evento', 'eletrônica'], ['live', 'quarentena', 'frio', 'aulas', 'head', 'famosos', 'agora', 'pinguim'], ['JavaScript', 'lista', 'matriz', 'postions'], ['pinguim']]
print(recomenda(tags))
