def mdc(x, y, contador, maximo): #máximo e contador começa com 1

    if x%contador == 0 and y%contador == 0:
        if contador == x and contador == y:
            return contador
        else:
            return mdc(x, y, contador+1, contador)
    else:
        if contador >= x or contador >= y:
            return maximo
        else:
            return mdc(x, y, contador+1, maximo)
        
print(mdc(15, 60, 1, 1))
            