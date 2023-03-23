def replace(l,x):
    for i in l:
        b = list(i)
        lista.append(b)
    for i in lista:
        i[-1] = x
        c= tuple(i)
        listat.append(c)
    return listat

lista = []
listat = []