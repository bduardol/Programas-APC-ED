def pescaria(n):
    peixe = input()
    if peixe == 'salmão':
        n = n*2
    while n > 0:
        n -= 1
        if peixe == 'salmão':
            print('Que salmão bonito que pesquei!')
        elif peixe == 'atum':
            print('Nossa, pesquei um atum gigante!')
        else:
            print('Nem sabia que esse peixe existia')
            n = n-n
    
pescaria(int(input()))