def triangulo(x,size):
    if x > 0:
        print(x * ' ',end="")
    print(size * '*')
    if size > 1:
        triangulo(x+1,size-2)
    return
        
triangulo(0,5)

    

