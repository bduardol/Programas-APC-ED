def crescimento(pa,pb,t1,t2):
    anos = 0
    t1 = t1/100
    t2 = t2/100
    while True:
        if t2 > t1:
            print('A nunca alcancara B.')
            break
        else:
            if pa < pb:
             roda = pa * t1
             pa = int(pa + roda)
             roda1 = pb * t2
             pb = int(pb + roda1)
             anos = anos + 1
            if pa >= pb and anos <= 1000:
                print(f'Vai alcancar em {anos} ano(s).')
                break
            elif pa >= pb and anos > 1000:
                print('Mais de um milenio.')
                break
        






pa,pb,t1,t2 = input().split()
pa = int(pa)
pb = int(pb)
t1 = float(t1)
t2 = float(t2)
crescimento(pa,pb,t1,t2)