def positivo(n):
    if n >= 0:
        return False
    else:
        return True


x = input()

if x == 'f':
    pass
else:
    x = int(x)
remov = x
acumulador = x
achou_positivo = False
cont = 0
if x != "f":
    while x != "f":
        if achou_positivo == positivo(x):
            cont += 1
            acumulador = acumulador + x
        x = input()
        if x == 'f':
            pass
        else:
            x = int(x)
    media_positivo = (acumulador - remov)/cont
    if x == "f":
        print(media_positivo)
else:
    print(0.0)
#cont += 1
