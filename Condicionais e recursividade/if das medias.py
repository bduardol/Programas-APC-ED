def ma(x,x1,x2):
    print('Aritimetica')
    result = (x + x1 + x2)/3
    print(f'{result:.2f}')
    return

def mp(x,x1,x2):
    print('Ponderada')
    p1,p2,p3 = map(int, input().split())
    result = (x * p1 + x1 * p2 + x2 * p3)/(p1+p2+p3)
    print(f'{result:.2f}')
    return

def mh(x,x1,x2):
    print('Harmonica')
    p1=(1/x)
    p2=(1/x1)
    p3=(1/x2)
    result=(3/(p1+p2+p3))
    print(f'{result:.2f}')
    return

def medias(a,b,c):
    qual = input()
    if qual == 'A':
        ma(a,b,c)
    elif qual == 'P':
        mp(a,b,c)
    elif qual == 'H':
        mh(a,b,c)
    else:
        print('Operacao inexistente')
        return

a,b,c = map(int, input().split())
medias(a,b,c)