class Node:
    def __init__(self,initdata):
        self.data = initdata
        self.next = None

    def getData(self):
        return self.data

    def getNext(self):
        return self.next

    def setData(self,newdata):
        self.data = newdata

    def setNext(self,newnext):
        self.next = newnext


class UnorderedList:
    def __init__(self):
        self.head = None

    def __str__(self):
        tmp = self.head
        lstr = ''
        while tmp != None:
            lstr += str(tmp.data) + ' '
            tmp = tmp.getNext()
            
        return lstr

    def isEmpty(self):
        return self.head == None

    def add(self,item):
        temp = Node(item)
        temp.setNext(self.head)
        self.head = temp

    def size(self):
        current = self.head
        count = 0
        while current != None:
            count = count + 1
            current = current.getNext()

        return count

    def search(self,item):
        current = self.head
        found = False
        while current != None and not found:
            if current.getData() == item:
                found = True
            else:
                current = current.getNext()

        return found
    
    def troca(self,item,index):
        pointer = self.head
        prox = None
        if index-1 == 0:
            node = Node(item)
            node.setNext(self.head)
            self.head = node
        else:
            for i in range(0,index-2):
                pointer = pointer.getNext()
            node = Node(item)
            node.setNext(pointer.getNext())
            pointer.setNext(node)
            
    def troca2(self,index):
        current = self.head
        previous = None
        found = False
        for i in range(index-1):
            previous = current
            current = current.getNext()
        if previous == None:
            self.head = current.getNext()
        else:
            previous.setNext(current.getNext())
            
    def final(self,index):
        current = self.head
        previous = None
        found = False
        if self.size() != 0:
            for i in range(self.size()-1):
                previous = current
                current = current.getNext()
            if previous == None:
                self.head = current.getNext()
            else:
                previous.setNext(current.getNext())
        else:
            self.head = index
            index.setNext(previous)
            
    def retornaF(self):
        valor = self.head
        for i in range(self.size() - 1):
            valor = valor.getData()
        return valor
   
    def retornaI(self):
        valor = self.head
        self.head = valor.getNext()
        return valor.getData()
        
    def retornaP(self,n):
        current = self.head
        previous = None
        found = False
        for i in range(index-1):
            previous = current
            current = current.getNext()
        valor = current.getData()
        if previous == None:
            self.head = current.getNext()
        else:
            previous.setNext(current.getNext())
            
        return valor
    
    def priF(self):
        ini = self.head
        print(" ")
        print(ini.getData())
        for i in range(self.size()):
            ini = ini.getNext()
            print(ini.getData())
            
    def remove(self,item):
        current = self.head
        previous = None
        found = False
        while not found:
            if current.getData() == item:
                found = True
            else:
                previous = current
                current = current.getNext()

        if previous == None:
            self.head = current.getNext()
        else:
            previous.setNext(current.getNext())
            
   
    
    
    
    
    
#L = UnorderedList()
#L.add(4)
#L.add(3)
#L.add(2)
#L.add(1)
#print(f'Lista: {L}')
#L.troca2(3)
#print(f'Lista: {L}')
#L.troca(5,3)
#print(f'Lista: {L}')


L = UnorderedList()
a=True
while a:
    comando = input().split()
    if comando[0] == 'I':
        v=comando[-1]
        L.add(v)
    elif comando[0] == 'F':
        v=comando[-1]
        L.final(v)
    elif comando[0] == 'P':
        L.troca2(L.size())
        print(l.retornaF())
        
    elif comando[0] == 'D':
        L.retornaI()
    elif comando[0] == 'E':
        n = comando[-1]
        L.retornaP(n)
    
    elif comando[0] == 'T':
        v=comando[0]
        n=comando[-1]
        L.troca2(v)
        L.troca(v,n)
        
    else:
        L.priF()
        a=False
    
    


