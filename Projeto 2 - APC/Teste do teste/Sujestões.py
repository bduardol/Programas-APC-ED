import csv
from collections import Counter
dados_dic={'Código':'','Nome':'','Turma':'','Ano-Período':'','Docente':'','Horário':'','Qtde Vagas Ofertadas':'','Qtde Vagas Ocupadas':'','Local':''}
dados=[]

def adicionar_dados(n):
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

def carga():
    pass

def diciplinas(n):
    diciplinas1=[]
    diciplinas_final=[]
    x=1
    for i in range(len(dados)):
        for j in range(i,len(dados)):
            if [dados[i]['Código'],dados[i]['Nome'],dados[i]['Turma']] == [dados[j]['Código'],dados[j]['Nome'],dados[j]['Turma']] and i!=j and x:
                if [dados[j]['Código'],dados[j]['Nome'],dados[j]['Turma'],dados[j]['Docente']] not in diciplinas1:
                    diciplinas1.append([dados[i]['Código'],dados[i]['Nome'],dados[i]['Turma'],dados[i]['Docente']])
                    diciplinas1.append([dados[j]['Código'],dados[j]['Nome'],dados[j]['Turma'],dados[j]['Docente']])
                    x=0
            elif [dados[i]['Código'],dados[i]['Nome'],dados[i]['Turma']] == [dados[j]['Código'],dados[j]['Nome'],dados[j]['Turma']] and i!=j:
                if [dados[j]['Código'],dados[j]['Nome'],dados[j]['Turma'],dados[j]['Docente']] not in diciplinas1:
                    diciplinas1.append([dados[j]['Código'],dados[j]['Nome'],dados[j]['Turma'],dados[j]['Docente']])    
        x=1
    #for i in diciplinas1:
        #print(i)
    for i in diciplinas1:
        i.pop()
        c= i[1] +','+ i[2] +','+ i[0]
        diciplinas_final.append(c)
    
    valor_repetidos=[]
    for i in diciplinas_final:
        #print(i)
        qnt= diciplinas_final.count(i)
        #print(type(qnt))
        if qnt > 1 and i+','+str(qnt) not in valor_repetidos:
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
        
while True:
    a = input()
    if a != 'FIM':
        inicio, arq_eou_cod= a.split()
    
    if a == 'FIM':
        break
    elif inicio == 'leia':
        adicionar_dados(arq_eou_cod)
        
    elif inicio == 'carga':
        carga(arq_eou_cod)
        
    elif inicio == 'matriculas':
        matricula(arq_eou_cod)
        
    elif inicio == 'disciplina':
        diciplinas(int(arq_eou_cod))
    
    
        
