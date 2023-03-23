peixe = ''
rede = []
def ultimacoisa(n):
    rede.append(peixe)
    
def printar():
    print('Hoje eu pesquei:')
    for i in range(len(rede)):
        print(rede[i])
    
    
    
    
while True:
    peixe = input()
    if peixe != 'acabou':
        ultimacoisa(peixe)
    else:
        printar()
        break