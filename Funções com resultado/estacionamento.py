def calcula_tiquete_estacionamento(a,b,c,d):
    '''1a e 2a hora - R$ 3,50 cada
    3a e 4a hora - R$ 4,10 cada
    5a hora em diante - R$ 4,60 cada'''
    valor1 = float(3.50)
    valor2 = float(4.10)
    valor3 = float(4.60)  
    if a == c and b == d:
        p = 2 * valor1
        k = 2 * valor2
        u = 20 * valor3
        l = p + k + u
        return l,24
    if c == 0:
        c = 24
    min_total_x1 = (a * 60) + b
    min_total_x0 = (c*60)+d
    minutos_valor = min_total_x0 - min_total_x1
    if minutos_valor < 0:
        min_total_x1 = 1440 - min_total_x1
        minutos_valor = min_total_x0 + min_total_x1
    hrs_pg = minutos_valor / 60
    if hrs_pg%1 > 0:
        hrs_pg = hrs_pg +1
    hrs_pg= int(hrs_pg)
    if hrs_pg <= 2:
        p = hrs_pg * valor1
        return p,hrs_pg
    elif  hrs_pg >=3 and hrs_pg <= 4:
        p = 2 * valor1
        k = (hrs_pg - 2) * valor2
        l = p + k
        return l,hrs_pg
    else:
        p = 2 * valor1
        k = 2 * valor2
        u = float((hrs_pg - 4) * valor3)
        l = p + k + u
        return l,hrs_pg
         
print(calcula_tiquete_estacionamento(23,45,0,30))