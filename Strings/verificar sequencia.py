def put(c):
    while c > 0:
        sequencia(input())
        c -= 1
        
def sequencia(n):
    n = list(n)
    posicao = []
    total0 = 0
    x = '1'
    
    for i in range(len(n)):
        if n[i] == x:
            posicao.append(i)
    #print(posicao)
    if posicao != []:    
        for i in range(posicao[0],posicao[-1]):
            if n[i] == '0':
                total0 += 1
    else:
         return print('0')
    print(total0)
    pass
    
put(int(input()))