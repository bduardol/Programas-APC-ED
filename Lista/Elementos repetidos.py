lista = []
listaint = []
lista = input().split()
for i in lista:
    listaint.append(int(i))

lista2 = sorted(set(listaint))
if len(listaint) == len(lista2):
    print(False)
else:
    print(True)