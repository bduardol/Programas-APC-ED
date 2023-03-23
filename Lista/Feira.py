feira = []
tabela_valor = []
erros=[]
cont = 0
b = 0
x=1
total = 0
def soma_alimentos():
    total = 0
    for i in range(len(feira)):
        fruta, valor = feira[i]
        valor = int(valor)
        x=1
        for j in range(len(tabela_valor)):
            fruta2, valor2 = tabela_valor[j]
            valor2 = float(valor2)
            if fruta == fruta2:
                b = valor*valor2
                total += b
                x=0
        if x:
            erros.append(fruta)
    return total
def printe_falta():
    
    
    pass

cont = int(input())
for i in range(cont):
    fruta = input().split()
    feira.append(fruta)

cont = int(input())
for i in range(cont):
    fruta = input().split()
    tabela_valor.append(fruta)

total = soma_alimentos()
for i in range(len(erros)):
    print(f'{erros[i]} esta em falta')
print(f'{total:.2f}')
