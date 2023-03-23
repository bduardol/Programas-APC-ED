def next_prim(ai, i): 
    i = i-1
    if i >= 1:
        i = i
        return next_prim(ai+1, i-1)
    return ai
     
def next(ai, i):
    if i == 1:
        return 0
    return next_prim(ai, i)

print(next(51, 101))