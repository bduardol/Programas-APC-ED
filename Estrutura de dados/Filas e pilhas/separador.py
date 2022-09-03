entrada = input().split()
palavras = []
numeros = []

for i in entrada:
    if i.isalpha():
        palavras.append(i)
    else:
        numeros.append(int(i))

if palavras != []:
    print("Palavras:")
    for i in range(len(palavras)):
        print(palavras.pop())
    print('\n')

if numeros != []:
    print("Palavras:")
    for i in range(len(numeros)):
        print(numeros.pop())
