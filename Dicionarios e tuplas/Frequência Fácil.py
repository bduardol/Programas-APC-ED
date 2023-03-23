alfabeto = 'abcdefghijklmnopqrstuvwxyz'
numeros = '0123456789'
dic_alf = {'a' : 0, 'b' : 0, 'c' : 0, 'd' : 0, 'e' : 0, 'f' : 0, 'g' : 0, 'h' : 0, 'i' : 0, 'j' : 0, 'k' : 0, 'l' : 0, 'm' : 0, 'n' : 0, 'o' : 0, 'p' : 0, 'q' : 0, 'r' : 0, 's' : 0, 't' : 0, 'u' : 0, 'v' : 0, 'w' : 0, 'x' : 0, 'y' : 0, 'z' : 0, '0' : 0, '1' : 0, '2' : 0, '3' : 0, '4' : 0, '5' : 0, '6' : 0, '7' : 0, '8' : 0, '9' : 0}

def sequencia(x):
    seq = list(x)
    qnt=int()
    l=[]
    n=[]
    for i in seq:
        if i.isdigit():
            n.append(int(i))
        else:
            l.append(i)           

    for i in l:
        qnt = l.count(i)
        dic_alf[i] = qnt
    
    for i in n:
        qnt = n.count(i)
        dic_alf[str(i)] = qnt
        

    for i in dic_alf:
        print(f'O caractere {i} aparece {dic_alf[i]} vez(es) na cadeia lida pelo programa :)')
        
sequencia(input())
        
