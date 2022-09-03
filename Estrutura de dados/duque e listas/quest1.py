class Deque:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def add_front(self, item):
        self.items.append(item)

    def add_rear(self, item):
        self.items.insert(0,item)

    def remove_front(self):
        return self.items.pop()

    def remove_rear(self):
        return self.items.pop(0)

    def size(self):
        return len(self.items)

deque = Deque()

def exibe_candidatos(lista, pos, ordem):
    if deque.size() != 0 and deque.size()>pos:
        if ordem == 'direta':
            for i in range(pos):
                lista.remove_front()
            for i in range(lista.size()):
                print(lista.remove_front())

        elif ordem == 'inversa':
            te = lista.size()-(pos+1)
            for i in range(te):
                lista.remove_rear()
            for i in range(lista.size()):
                print(lista.remove_rear())