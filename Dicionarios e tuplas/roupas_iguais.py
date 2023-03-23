from collections import Counter
nãoseipraq=input()
a=input().split()
dici= {}
x=0
c = Counter(a)
for n in a:
    if c[n]>1:
        print('WOW')
        x=0
        break
    else:
        x=1        
if x:
    print('MEH')