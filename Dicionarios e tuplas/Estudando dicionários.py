di=[]
d = []
a=[]

def adicionar_dicionario(n):
    for i in range(n):
        entrada = input().split('=')
        d.append(entrada)
        
    di = dict(d)
    chave= input()
    for i in di:
        if di[i] == chave:
            a.append(i)
x= input()
adicionar_dicionario(int(x))
print(a)

