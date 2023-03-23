nome = input()
lista = []
fim = 'fim'
while nome != fim:
    lista.append(nome)
    nome = input()
lista.sort()
temp = ""
conta = 0
saida = []
for i in range(len(lista)):
    if i == temp:
        conta += 1
    else:
        if conta < i:
            saida + [temp , conta]
            conta = 1
    temp = i
for i in range(len(saida)):
    print(i[0], i[1])