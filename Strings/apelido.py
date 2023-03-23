def apelido(nome):
    if ' ' in nome:
        a = []
        a = nome.split()
        b = a[1]
        a = a[0]
        c = a[:2]+b[:2]
        print(c)
    elif len(nome) > 3:
        print(nome[:3])
    elif len(nome) == 3:
        print(nome[:2])
        
        
apelido(input())