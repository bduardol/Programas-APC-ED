def ovini(l,r):
    vistos = 0
    while l <= r:
        aux = (l ** 0.5)%1
        if aux == 0.0:
            vistos = vistos + 1
        l = l + 1
    print(f'{vistos}')
        
l,r = (map(int, input().split()))
ovini(l,r)