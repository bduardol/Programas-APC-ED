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
    
    def sizeExp(self,item):
        current = self.head
        count = 0
        for i in range(L.size()):
            if current.getData() == item:
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


    def removePosition(self,item):
        current = self.head
        previous = None
        found = False
        cont = 0
        while cont != 2:
            if current.getData() == item:
                if(cont == 0):
                    found = True
                    previous = current
                    current = current.getNext()
                cont = cont + 1
                found = True
            else:
                previous = current
                current = current.getNext()

        if previous == None:
            self.head = current.getNext()
        else:
            previous.setNext(current.getNext())
            
            
            
def removerSegundaOcorrencia(lista, num):
    conf = lista.sizeExp(num)
    if conf >=2 :
        lista.removePosition(num)
    return lista



L = UnorderedList()
L.add(1)
L.add(2)
L.add(3)
L.add(2)
L.add(4)
L.add(2)
L.add(5)
L.add(2)
L.add(6)
L.add(2)
L.add(7)
L = removerSegundaOcorrencia(L, 2)
print(f'Lista: {L}')










'''L = UnorderedList()
L.add(1)
L.add(2)
print(L.sizeExp(2))
L.getData(2)
L = removerSegundaOcorrencia(L, 2)
print(f'Lista: {L}')'''