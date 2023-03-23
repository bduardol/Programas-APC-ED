def divisivel(a):
    v1 = a%2
    v2 = a%3
    if (v1 == 0) and  (v2 == 0):
        print(f'Divisível por 2 e 3!')
    else:
        print(f'Não é divisível por 2 e 3...')
    
a = int(input())
divisivel(a)