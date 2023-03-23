lista = []
sapatos = []
def colocar_lista_em_ordem(n):
    for i in range(len(n)):
        for j in range(len(n)):
            if n[i] < n[j]:
                aux = n[i]
                n[i] = n[j]
                n[j] = aux


pe_do_menino = int(input())
lista = input().split()

for i in lista:
    sapatos.append(int(i))
colocar_lista_em_ordem(sapatos)
aux = 0
if sapatos[0] < pe_do_menino:
    for i in range(len(sapatos)):
        if sapatos[i] < pe_do_menino:
            aux += 1
    if aux == len(sapatos):
        print('-1')
        

for i in range(len(sapatos)):
    if sapatos[i] >= pe_do_menino:
        print(i)
        break
            














