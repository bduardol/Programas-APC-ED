def retangulo1(a,b):
    base = int(a*b)
    print(f'O retangulo tem {base} de area')
    return

def losango1(a,b):
    base = int((a*b)/2)
    print(f'O losango tem {base} de area')
    return

def area(a,b,c):
    if c == 'losango':
        losango1(a,b)
    elif c == 'retangulo':
        retangulo1(a,b)
    else:
        return
    
area(10, 2, 'losango')