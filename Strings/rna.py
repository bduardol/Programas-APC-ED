'''rna1 = input ('Insira o RNA 1: ')
rna2 = input ('Insira o RNA 2: ')
    
differences = 0

for r1, r2 in zip(rna1, rna2):
    if r1 != r2:
        differences += 1
        
print(differences)'''

k = '1223'
h = '5423'
t = '5789'
x = 0
for r, m,n in zip(k, h, t):
    if r != m != n:
        x += 1
    print(x)