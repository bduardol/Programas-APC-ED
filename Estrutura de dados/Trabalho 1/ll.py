
class Queue:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.insert(0,item)
        
    def enqueueF(self, item):
        self.items.append(item)

    def dequeue(self):
        return self.items.pop()

    def size(self):
        return len(self.items)
    
    def troca(self):        
        primeiro = self.items[0]
        segundo = self.items[1]
        #print(self.items)
        #print(primeiro, segundo)
        if primeiro > segundo:
            self.enqueueF(self.items.pop(1))
        else:
            self.enqueueF(self.items.pop(0))
    def mano(self):
        x=True
        for i in self.items:
            if x:
                c = str(i)
                x =False
            else:
                c+=str(i)
        print(c)
        for i in range(len(self.items)):
            self.items.pop()
        
def crip(lista):
    b=[]
    p=0
    x=1
    for i in lista:
        if i == '(':
            x=1
            p=0
        elif i == ')':
            x=0
            p=0
        if x:
            b.insert(p,i)
            p+=1
        else:
            b.append(i)
    
    while '(' in b:
        b.remove('(')
    while ')' in b:
        b.remove(')')
        
    x = True
    for i in b:
        if x:
            c = i
            x =False
        else:
            c+=i
    print(c)
   
a = Queue()
listaMemoria = []

while True:
    comando = input().split()
    if comando[0] == 'stop':
        pro = len(listaMemoria)
        print(f'{pro} processo(s) órfão(s).')
        break
    elif comando[0] == 'go':
        if listaMemoria != []:
            listaMemoria.sort(reverse = False)
            comando1 = listaMemoria.pop(0)
            if comando1[1] == 'dekey':
                idx = len(comando1[3])
                for i in range(len(comando1[3])):
                    idx -= 1
                    a.enqueue(comando1[3][idx])
                for i in range(comando1[2]):
                    a.troca()
                a.mano()
            else:
                crip(comando1[2])
    elif comando[0] == 'enqueue':
        for i in range(int(comando[1])):
            comando = input().split()
            if comando[1] == 'dekey':
                listaMemoria.append([int(comando[0]),comando[1],int(comando[2]), list(map(int, comando[3:]))])
            else:
                listaMemoria.append([int(comando[0]),comando[1],comando[2]])
        listaMemoria.sort(reverse = True)
        #print(listaMemoria)
        pass





