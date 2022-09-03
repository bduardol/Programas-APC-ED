class Deque:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def addFront(self, item):
        self.items.append(item)

    def addRear(self, item):
        self.items.insert(0,item)

    def removeFront(self):
        return self.items.pop()

    def removeRear(self):
        return self.items.pop(0)

    def size(self):
        return len(self.items)
    
    
    
string = input()

deque = Deque()
fim=''
for i in string:
    if i == '*':
        a = deque.removeFront()
        fim +=a
        pass
    elif i == '+':
        b = deque.removeRear()
        fim+=b
        pass
    elif i.isnumeric():
        deque.addRear(i)
    else:
        deque.addFront(i)
    
print(fim)


