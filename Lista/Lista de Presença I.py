def printar_lista(n):
    nomesf = sorted(nomes)
    print(len(nomesf))
    print(nomesf)
nomes = []
nomesf = []
nome = ''   
while True:
    nome = input()
    if nome == 'EOF':
        printar_lista(nomes)
        break
    else:
        nomes.append(nome)
        
        
    
    