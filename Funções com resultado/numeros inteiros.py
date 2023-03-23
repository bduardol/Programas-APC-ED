def media(n, cont, soma):
    if n == 0:
        return 0
    if cont < n:
        cont += 1
        i = int(input())
        soma+=i
        return media(n, cont, soma)
    else:
        return soma / n
    
print(media(3, 0, 0))