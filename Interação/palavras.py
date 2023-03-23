n = int(input())
i = 0
ini = 0
for i in range(n):
    if n <= 0:
        break
    x = input()
    if ini != 0:
        ini = ini + x
    else:
        ini = x
    i = i + 1
    
if n != 0:
    print(ini)
    
