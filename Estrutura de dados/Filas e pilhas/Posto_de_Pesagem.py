class Queue:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.insert(0,item)

    def dequeue(self):
        return self.items.pop()

    def size(self):
        return len(self.items)
tempo = 0
qnt, repe, peso = map(int, input().split())
fila = Queue()
carro = input().split()
carros = [int(i) for i in carro]
for i in range(0, qnt):
    fila.enqueue(carros[i])

while qnt != 0:
    c = fila.dequeue()
    if c > peso:
        c -= 2
        fila.enqueue(c)
        tempo += 10
    else:
        qnt -= 1
        tempo +=5
    if repe > 1 and fila.isEmpty() == False:
        x=repe
        if x > 0:
            for i in range(x):
                fila.dequeue()
                tempo +=1
                qnt -= 1
                x-=1

print(tempo)