def divisivel(x,y):
    teste = x/y
    if(int(teste)==teste):
        print('x eh divisivel por y')
    else:
        print('x nao eh divisivel por y')
        
x = int(input())
y = int(input())
divisivel(x,y)