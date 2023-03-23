erros=[]
all_codigos = []
todos_codigos_ativos = []

horariosM = ['08:00 - 08:55', '08:55 - 09:50','10:00 - 10:55','10:55 - 11:50', '12:00 - 12:55' ]
horariosT = ['12:55 - 13:50','14:00 - 14:55','14:55 - 15:50','16:00 - 16:55','16:55 - 17:50','18:00 - 18:55']
horariosN =['19:00 - 19:50','19:50 - 20:40','20:50 - 21:40','21:40 - 22:30']

hrvazio = '          |'

manha = []
tarde = []
noite = []

for i in range(5):
    linha = []
    for j in range(6):
        linha.append(0)
    manha.append(linha)
    
for i in range(6):
    linha = []
    for j in range(6):
        linha.append(0)
    tarde.append(linha)
    
for i in range(4):
    linha = []
    for j in range(6):
        linha.append(0)
    noite.append(linha)
    
def adicionar_codigo(n):
    all_codigos.append(n)
    
    for i in range(len(todos_codigos_ativos)):
        if n not in todos_codigos_ativos[i]:
            todos_codigos_ativos.append(n)
    if todos_codigos_ativos == []:
        todos_codigos_ativos.append(n)
        
    partes = n.split(' ')
    sinal, codigo2, hora = partes[0], partes[1], partes[2:]
    for i in range(len(hora)):
        if 'M' in hora[i]:
            dia, hor = hora[i].split('M')
            """for dia in range(2,7):
                for hou in range(1,5):
                    manha[hou-1][dia-2] = codigo"""
            for i in dia:
                for j in hor:
                    if manha[int(j)-1][int(i)-2] == 0:
                        manha[int(j)-1][int(i)-2] = codigo2
                    else:
                        erros.append(codigo)
                        return 0
                        
    for i in range(len(hora)):
        if 'T' in hora[i]:
            dia, hor = hora[i].split('T')
            """for dia in range(2,7):
                for hou in range(1,5):
                    manha[hou-1][dia-2] = codigo"""
            for i in dia:
                for j in hor:
                    if tarde[int(j)-1][int(i)-2] == 0:
                        tarde[int(j)-1][int(i)-2] = codigo2
                    else:
                        erros.append(codigo)
                        return 0

    for i in range(len(hora)):
        if 'N' in hora[i]:
            dia, hor = hora[i].split('N')
            """for dia in range(2,7):
                for hou in range(1,5):
                    manha[hou-1][dia-2] = codigo"""
            for i in dia:
                for j in hor:
                    if noite[int(j)-1][int(i)-2] == 0:
                        noite[int(j)-1][int(i)-2] = codigo2
                    else:
                        erros.append(codigo)
                        return 0
             
def remover_codigo(n):
    
    partes = n.split(' ')
    sinal, codigo2, hora = partes[0], partes[1], partes[2:]
    for i in range(len(hora)):
        if 'M' in hora[i]:
            dia, hor = hora[i].split('M')
            for i in dia:
                for j in hor:
                    if manha[int(j)-1][int(i)-2] == codigo2:
                        manha[int(j)-1][int(i)-2] = 0
                    else:
                        erros.append(codigo)
                        return 0
                        
    for i in range(len(hora)):
        if 'T' in hora[i]:
            dia, hor = hora[i].split('T')  
            for i in dia:
                for j in hor:
                    if tarde[int(j)-1][int(i)-2] == codigo2:
                        tarde[int(j)-1][int(i)-2] = 0
                    else:
                        erros.append(codigo)
                        return 0

    for i in range(len(hora)):
        if 'N' in hora[i]:
            dia, hor = hora[i].split('N')
            for i in dia:
                for j in hor:
                    if noite[int(j)-1][int(i)-2] == codigo2:
                        noite[int(j)-1][int(i)-2] = 0
                    else:
                        erros.append(codigo)
                        return 0
    pass

def printar_codigo(n):
    x=1
    b=1
    l = 0
    for i in range(len(erros)):
        print(f'!({erros[i]})')
    print('+---------------+----------+----------+----------+----------+----------+----------+')
    print('|               | Seg      | Ter      | Qua      | Qui      | Sex      | Sab      |')
    print('+---------------+----------+----------+----------+----------+----------+----------+')
    for i in range(len(manha)):
        x,b=1,1
        for c in range(len(manha[i])):
            if manha[i][c] != 0 and x:
                print(f'| {horariosM[i]} |',end="")
                x=0
            if manha[i][c] != 0 and b:
                for d in range(len(manha[i])):
                    if manha[i][d] == 0:
                        print(f'{hrvazio}',end="")
                    if manha[i][d] != 0:
                        print(f' {manha[i][d]} |',end="")
                        l = 1
                b=0
        if l:
            print(f'\n+---------------+----------+----------+----------+----------+----------+----------+')
            l = 0
            
    for i in range(len(tarde)):
        x,b=1,1
        for c in range(len(tarde[i])):
            if tarde[i][c] != 0 and x:
                print(f'| {horariosT[i]} |',end="")
                x=0
            if tarde[i][c] != 0 and b:
                for d in range(len(tarde[i])):
                    if tarde[i][d] == 0:
                        print(f'{hrvazio}',end="")
                    if tarde[i][d] != 0:
                        print(f' {tarde[i][d]} |',end="")
                        l = 1
                b=0
        if l:
            print(f'\n+---------------+----------+----------+----------+----------+----------+----------+')
            l = 0
            
    for i in range(len(noite)):
        x,b=1,1
        for c in range(len(noite[i])):
            if noite[i][c] != 0 and x:
                print(f'| {horariosN[i]} |',end="")
                x=0
            if noite[i][c] != 0 and b:
                for d in range(len(noite[i])):
                    if noite[i][d] == 0:
                        print(f'{hrvazio}',end="")
                    if noite[i][d] != 0:
                        print(f' {noite[i][d]} |',end="")
                        l = 1
                b=0
        if l:
            print(f'\n+---------------+----------+----------+----------+----------+----------+----------+')
            l = 0

while True:
    codigo = (input())
    if codigo == 'Hasta la vista, beibe!':
        break
    if codigo[0] == '?':
        printar_codigo(codigo[0])
        erros = []
    elif codigo[0] == '+':
        adicionar_codigo(codigo)
    elif codigo[0] == '-':
        remover_codigo(codigo)