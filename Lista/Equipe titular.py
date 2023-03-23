soma = 0
lista = input().split()
lista2=[]

for i in lista:
    lista2.append(int(i))
for i in range(len(lista2)):
        for j in range(len(lista2)):
            if lista2[i] > lista2[j]:
                aux = lista2[i]
                lista2[i] = lista2[j]
                lista2[j] = aux
                
for i in range(0,12):
    soma += lista2[i]
print(soma)
    