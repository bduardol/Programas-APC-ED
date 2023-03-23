def next(ai,i):
    if i%2 == 1:
        i = i*(-1)
    result = ai + i
    return result
    
print(next(51, 101))