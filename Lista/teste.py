horario_dias = []
materia = []
erro = []
horario=['0','| 08:00 - 08:55 ' #m1 0
, '| 08:55 - 09:50 '#m2 1
, '| 10:00 - 10:55 '#m3 
, '| 10:55 - 11:50 '#m4
, '| 12:00 - 12:55 '#m5
, '| 12:55 - 13:50 '#t1
, '| 14:00 - 14:55 '#t2
, '| 14:55 - 15:50 '#t3
, '| 16:00 - 16:55 '#t4
, '| 16:55 - 17:50 '#t5         
, '| 18:00 - 18:55 '#t6
, '| 19:00 - 19:50 '#n1
, '| 19:50 - 20:40 '#n2
, '| 20:50 - 21:40 '#n3
, '| 21:40 - 22:30 ']#n4
dias_da_semana = [['|              ','| Seg     ','| Ter     ','| Qua     ','| Qui     ','| Sex     ','| Sab      |'], ['|         ','|         ','|         ','|         ','|         ','|         '],['|         ','|         ','|         ','|         ','|         ','|         '],['|         ','|         ','|         ','|         ','|         ','|         '],['|         ','|         ','|         ','|         ','|         ','|         '],['|         ','|         ','|         ','|         ','|         ','|         '],['|         ','|         ','|         ','|         ','|         ','|         '],['|         ','|         ','|         ','|         ','|         ','|         '],['|         ','|         ','|         ','|         ','|         ','|         '],['|         ','|         ','|         ','|         ','|         ','|         '],['|         ','|         ','|         ','|         ','|         ','|         '],['|         ','|         ','|         ','|         ','|         ','|         '],['|         ','|         ','|         ','|         ','|         ','|         '],['|         ','|         ','|         ','|         ','|         ','|         '],['|         ','|         ','|         ','|         ','|         ','|         '],['|         ','|         ','|         ','|         ','|         ','|         ']] # os 4 horarios da noite
def adicionar(horario_dias, materia, turma_horario):#sinal, horario):    
    ocupado = False
    for x in horario_dias[0:len(horario_dias)]:
        if 'M' in x:
            manha = x.index('M')
            dias_e_horarios = x.split(x[manha]) # me da os dias e horario em list['246','23']
            dias_da_manha = [int(x) -2 for x in dias_e_horarios[0]] # me da somente os dias como numeros
            horas_da_manha = [int(x)  for x in dias_e_horarios[1]]# me da somente os horarios como numeros
            for i in dias_da_manha:
                for j in horas_da_manha:
                    if dias_da_semana[j][i] != '|         ': #verifica se esta vazio
                        ocupado = True         
        elif 'T' in x:
            tarde = x.index('T')
            dias_e_horarios = x.split(x[tarde])
            dias_da_tarde= [int (x)-2 for x in dias_e_horarios[0]]
            horas_da_tarde = [int(x)+5 for x in dias_e_horarios[1]]
            for i in dias_da_tarde:
                for j in horas_da_tarde:
                    if dias_da_semana[j][i] != '|         ':
                        ocupado = True
        elif 'N' in x:    
            noite = x.index('N')
            dias_e_horarios = x.split(x[noite])
            dias_da_noite= [int (x) -2 for x in dias_e_horarios[0]]
            horas_da_noite = [int(x)+11 for x in dias_e_horarios[1]] 
            for i in dias_da_noite: 
                for j in horas_da_noite:
                   if dias_da_semana[j][i] != '|         ':
                       ocupado = True

    if ocupado == False:
        for x in horario_dias[0:len(horario_dias)]:
            if 'M' in x:
                manha = x.index('M')
                dias_e_horarios = x.split(x[manha]) #list['246','12']
                dias_da_manha = [int(x) -2 for x in dias_e_horarios[0]] 
                horas_da_manha = [int(x)  for x in dias_e_horarios[1]]
                for i in dias_da_manha: # i representa 0,2,4('246')
                    for j in horas_da_manha: # j representa 6,7('12')
                        dias_da_semana[j][i] = '| '+ materia #ocupa os dias/horario da matriz refente a i e j 
            elif 'T' in x:
                tarde = x.index('T')
                dias_e_horarios = x.split(x[tarde])
                dias_da_tarde= [int (x)-2 for x in dias_e_horarios[0]]
                horas_da_tarde = [int(x)+5 for x in dias_e_horarios[1]]
                for i in dias_da_tarde:
                    for j in horas_da_tarde:
                       dias_da_semana[j][i] = '| ' + materia
                    
            elif 'N' in x:    
                noite = x.index('N')
                dias_e_horarios = x.split(x[noite])
                dias_da_noite= [int (x) -2 for x in dias_e_horarios[0]]
                horas_da_noite = [int(x)+11 for x in dias_e_horarios[1]]
                for i in dias_da_noite:
                    for j in horas_da_noite: 
                        dias_da_semana[j][i] = '| ' + materia         
    else:
        erro.append(codigo)
        print(f'!({turma_horario})')
   
    
def remover(horario_dias, materia, turma_horario):
    ocupado = False
    for x in horario_dias[0:len(horario_dias)]:
        if 'M' in x:
            manha = x.index('M')
            dias_e_horarios = x.split(x[manha]) # me da os dias e horario em list['246','23']
            dias_da_manha = [int(x) -2 for x in dias_e_horarios[0]] # me da somente os dias como numeros
            horas_da_manha = [int(x)  for x in dias_e_horarios[1]]# me da somente os horarios como numeros
            for i in dias_da_manha:
                for j in horas_da_manha:
                    if dias_da_semana[j][i] != materia: #verifica se há alguma disciplina na posição
                        ocupado = True
        elif 'T' in x:
            tarde = x.index('T')
            dias_e_horarios = x.split(x[tarde])
            dias_da_tarde= [int (x)-2 for x in dias_e_horarios[0]]
            horas_da_tarde = [int(x)+5 for x in dias_e_horarios[1]]
            for i in dias_da_tarde:
                for j in horas_da_tarde:
                    if dias_da_semana[j][i] != materia:
                        ocupado = True
        elif 'N' in x:    
            noite = x.index('N')
            dias_e_horarios = x.split(x[noite])
            dias_da_noite= [int (x) -2 for x in dias_e_horarios[0]]
            horas_da_noite = [int(x)+11 for x in dias_e_horarios[1]] 
            for i in dias_da_noite: 
                for j in horas_da_noite:
                   if dias_da_semana[j][i] != materia:
                       ocupado = True

    if ocupado == False: 
        for x in horario_dias[0:len(horario_dias)]:
            if 'M' in x:
                manha = x.index('M')
                dias_e_horarios = x.split(x[manha]) #list['246','12']
                dias_da_manha = [int(x) -2 for x in dias_e_horarios[0]] 
                horas_da_manha = [int(x)  for x in dias_e_horarios[1]]
                for i in dias_da_manha: # i representa 0,2,4('246')
                    for j in horas_da_manha: # j representa 6,7('12')
                        dias_da_semana[j][i] = '|         ' #troca a materia por vazio
            elif 'T' in x:
                tarde = x.index('T')
                dias_e_horarios = x.split(x[tarde])
                dias_da_tarde= [int (x)-2 for x in dias_e_horarios[0]]
                horas_da_tarde = [int(x)+5 for x in dias_e_horarios[1]]
                for i in dias_da_tarde:
                    for j in horas_da_tarde:
                       dias_da_semana[j][i] = '|         '
                    
            elif 'N' in x:    
                noite = x.index('N')
                dias_e_horarios = x.split(x[noite])
                dias_da_noite = [int (x) -2 for x in dias_e_horarios[0]]
                horas_da_noite = [int(x)+11 for x in dias_e_horarios[1]]
                for i in dias_da_noite:
                    for j in horas_da_noite: 
                        dias_da_semana[j][i] = '|         '           
    else:
        print(f'!({turma_horario})')
        
def grade_horaria(dias_da_semana, horario_dias, materia):
    if erro != []:
        for i in range(len(erro)):
            print(f'!{erro[i]}')
    print('+---------------+----------+----------+----------+----------+----------+----------+')
    print(*dias_da_semana[0])
    print('+---------------+----------+----------+----------+----------+----------+----------+')
    for i in range(1,len(dias_da_semana)):
        if dias_da_semana[i] != ['|         ','|         ','|         ','|         ','|         ','|         ']:
            print(horario[i],end="")
            print(*dias_da_semana[i], '|')
            print('+---------------+----------+----------+----------+----------+----------+----------+')
    
#possivel função aqui
while True:
    #print(*dias_da_semana, sep='\n')
    turma_horario = input("Turma e horario? ")
    if turma_horario == 'hasta':
        break
    elif turma_horario.split()[0] == '+' or turma_horario.split()[0] == '-':
        materia = turma_horario.split()[1]
        horario_dias = turma_horario.split()[2::]
        if turma_horario.split()[0] == '+':
            adicionar(horario_dias, materia, turma_horario)
        elif turma_horario.split()[0] == '-':
            remover(horario_dias, materia, turma_horario)
        elif turma_horario == '?':
                grade_horaria(dias_da_semana, horario_dias, materia)
    else:
        if turma_horario == '?':
            grade_horaria(dias_da_semana, horario_dias, materia) 
