def resto(x,y):
    resto = x%y
    if resto == 0:
        print(f'Divisao inteira')
    else:
        par_ou_impar(resto)

def par_ou_impar(resto):
    if resto == 2:
        print(f'Par')
    else:
        print(f'Impar')

x = int(input())
y = int(input())
resto(x,y)