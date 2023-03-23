cori = '0000000'
sp = '1111111'

def fultebol(n):
    x = 0
    b = 0
    if sp in n:
        x = 1
    if cori in n:
        b = 1
    if x == 0 and b == 0:
        print('BORA UM VIRTUAL NO CODEFORCES')
    elif x == 1 and b == 0:
        print('VAMO TRICOLOR')
    elif x == 0 and b == 1:
        print('VAI TIMAO')
    else:
        print('JOGO PESADO')
        
fultebol(input())
        