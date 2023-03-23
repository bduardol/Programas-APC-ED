primeiralinha={'nome':'','telefone':'','preço':''}
dici=[]
final=[]

def telefone(n):
    for linhas in n:
        primeiralinha.clear()
        primeiralinha['nome']=linhas[0]
        primeiralinha['telefone']=linhas[1]
        primeiralinha['preço']=linhas[2]
        dici.append(primeiralinha.copy()) #novo

    from collections import Counter
    c = Counter((dici[d]['telefone']) for d in range(4))
    print(c)
    duplicates = []
    print(c)
    for d in dici:
        if c[(d['telefone'])] > 1:
            duplicates.append(d)
    duplicates.append (d)

    final = [[d['telefone']] for d in duplicates]
    print(final)

a=[]
lista=[]
for i in range(4):
    for i in range(3):
        c=input()
        a.append(c)
    lista.append(a)

telefone(lista)
