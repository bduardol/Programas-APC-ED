import csv
from collections import Counter
dados_dic={'Código':'','Nome':'','Turma':'','Ano-Período':'','Docente':'','Horário':'','Qtde Vagas Ofertadas':'','Qtde Vagas Ocupadas':'','Local':''}
dados=[]
arq=[]

def adicionar_dados(n):
    if n not in arq:
        with open(n, 'r',encoding='UTF-8') as arquivo:
            arquivo_csv = csv.reader(arquivo, delimiter=",")
            for linhas in arquivo_csv:
                dados_dic.clear()
                dados_dic['Código']=linhas[0]
                dados_dic['Nome']=linhas[1]
                dados_dic['Turma']=linhas[2]
                dados_dic['Ano-Período']=linhas[3]
                dados_dic['Docente']=linhas[4]
                dados_dic['Horário']=linhas[5]
                dados_dic['Qtde Vagas Ofertadas']=linhas[6]
                dados_dic['Qtde Vagas Ocupadas']=linhas[7]
                dados_dic['Local']=linhas[8]
                dados.append(dados_dic.copy())
            del dados[0]
            #print(dados)

def carga(n):
    listas_de_materias=[]
    listas_de_materias_final=[]
    nomeh=''
    
    for i in n:
        nomeh+=i
        nomeh+=' '
    nomeh= nomeh[:-1]
    for i in dados:
        nome = i['Docente']
        no = nome.split('(')
        me = no[0]
        nome= me[:-1]
        if nomeh == nome:
            c=i['Docente']
            num = [j for j in c if j.isdigit()]
            if len(num) > 1:    
                card=''
                for j in num:
                    card+=j
            else:
                card= num[0]
            
        if nomeh == nome:
            b= [i['Nome'],i['Código'],i['Turma'],int(i['Qtde Vagas Ocupadas']),int(card)]
            listas_de_materias.append(b)
    #print(listas_de_materias)

    for i in listas_de_materias:
        if i not in listas_de_materias_final:
            listas_de_materias_final.append(i)
    #print(listas_de_materias_final)
            
    '''Print da  primeria parte'''
    listas_de_materias_final = sorted(listas_de_materias_final)
    aux=''
    aux_in=1
    if len(listas_de_materias_final) > 0:
        print(f'{nomeh}:')
        for i in listas_de_materias_final:
            if i[0] != aux:
                print(f' * {i[0]} ({i[1]}):')
                print(f'     Turma {i[2]}: {i[4]}h ({i[3]} alunos)')
                aux_in = 0
                aux = i[0]
            elif i[0] != aux:
                print(f' * {i[0]} ({i[1]}):')
                aux = i[0] 
            elif i[0]==aux:
                print(f'     Turma {i[2]}: {i[4]}h ({i[3]} alunos)')
                
        '''print parte 2'''
        horas=int()
        alunos=int()
        for i in listas_de_materias_final:
            if i[3] >=6:
                horas+= i[4]
                alunos+= i[3]
        media= (horas/alunos)
        print(f'[Carga total considerada: {horas}h ({media:.2f}h/aluno)]')
    
    else:
        print(f'No hay {nomeh}...')


def diciplinas(n):
    final=[]
    if n>=2:
        from collections import Counter
        key_counts = Counter((d['Código'], d['Turma']) for d in dados)
        duplicate_values = []
        for d in dados:
          if key_counts[(d['Código'], d['Turma'])] > 1:
            duplicate_values.append (d)
        final = [[d['Código'], d['Nome'], d['Turma']] for d in
        duplicate_values]
    else:
        from collections import Counter
        for i in dados:
            c=[]
            c.append(i['Código'])
            c.append(i['Nome'])
            c.append(i['Turma'])
            final.append(c)
            
    final2=[]
    for i in final:
        c= i[1] +','+ i[2] +','+ i[0]
        final2.append(c)
  
    valor_repetidos=[]       
    for i in final2:
        #print(i)
        qnt= final2.count(i)
        #print(type(qnt))
        if qnt > 0 and i+','+str(qnt) not in valor_repetidos:
            valor_repetidos.append(i+','+str(qnt))
    
   
    valor_repetidos = sorted(valor_repetidos)
    dados_final_print=[]
    for i in valor_repetidos:
        b=i.split(',')
        if int(b[3]) >= int(n):
            dados_final_print.append(i)     
    aux=''
    aux_in=1
    if len(dados_final_print) > 0:
        print(f'Turmas com pelo menos {n} docentes:')
    else:
        print(f'No hay {n}...')
        
    for i in dados_final_print:
        i=i.split(',')
        if int(i[3]) >= int(n):
            if i[0] != aux and aux_in:
                print(f' * {i[0]} ({i[2]}): {i[1]} ({i[3]})',end="")
                aux_in = 0
                aux = i[0]
            elif i[0] != aux:
                print(f'\n * {i[0]} ({i[2]}): {i[1]} ({i[3]})',end="")
                aux = i[0] 
            elif i[0]==aux:
                print(f', {i[1]} ({i[3]})',end="") 
    
    dados_final_print.clear()
    valor_repetidos.clear()
    valor_repetidos.clear()
    final.clear()
    final2.clear()

def matricula(n):
    lista = []
    lista_zero = []
    lista_um=[]
    qnt=int()
    w=0
    turmalist=[]
    for i in n:
        turmalist=[]
        for j in dados:
            nome=j['Nome']
            if i == j['Código'] and j['Turma'] not in turmalist:
                qnt+=int(j['Qtde Vagas Ocupadas'])
                turmalist.append(j['Turma'])
                
        for c in dados:
            if i == c['Código']:
                w=c['Nome']
                break
            
        d=[qnt,w,i]
        lista.append(d)
        qnt=0
    for i in lista:
        if int(i[0]) == 0:
            lista_zero.append(i)
    for i in lista:
        if int(i[0]) > 0:
            lista_um.append(i)
    #print(lista_zero)
    #print(lista_um)
    
    lista_um.sort(reverse = True)
    ve_se_ta_repetido=[]
    x=0
    n=''
    for i in lista_um:
            if i[0] not in ve_se_ta_repetido:
                ve_se_ta_repetido.append(i[0])
                
            else:
                n=i[0]
                x=1
                break
    #print(n)
        
    posicoes=[]

    if x:
        for i in range(len(lista_um)):
            if lista_um[i][0] == n:
                posicoes.append(i)
            for j in range(i,len(posicoes)):
                if lista_um[j][0] != n:
                    posicoes.append(j)
                    break
                break
            break
    #print(posicoes)
    
    if len(posicoes) == 1:
        lista_um = sorted(lista_um)
    elif len(posicoes) == 2:
        p1=posicoes[0]
        p2=posicoes[1]-1 
        lista_um = sorted(lista_um[p1:p2])






    
    if lista_zero != []:
        for i in lista_zero:
            if i[0] == 0:
                print(f'No hay {i[2]}...')
    if lista_um != []:
        for i in lista_um:
            if i[0]>0:
                print(f'{i[0]} matriculados em {i[1]} ({i[2]})')

            
    

while True:
    a = input()
    if a != 'FIM':
        termos = a.split()
        inicio, arq_eou_cod= termos[0], termos[1:]
    
    if a == 'FIM':
        break
    elif inicio == 'leia':
        adicionar_dados(arq_eou_cod[0])
        
    elif inicio == 'carga':
        carga(arq_eou_cod)
        
    elif inicio == 'matriculas':
        matricula(arq_eou_cod)
        
    elif inicio == 'disciplina':
        diciplinas(int(arq_eou_cod[0]))
    
    
        
