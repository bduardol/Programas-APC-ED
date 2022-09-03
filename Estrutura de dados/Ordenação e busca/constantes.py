lista = []
while True:
    entrada = int(input())
    if entrada == 0:
        break
    else:
        for i in range(entrada):
            vei = input().split(' = ')
            lista.append(tuple([float(vei[-1]),vei[0]]))
        lista.sort()
        
        x=0
        for i in  range(len(lista)):
            a = lista.pop(0)
            if x:
                print(f'\n{a[-1]}', end="")
            else:
                print(a[-1], end="")
            if lista != []:
                print(' < ',end="")
            else:
                break
        x = 1
        
                        
        
        