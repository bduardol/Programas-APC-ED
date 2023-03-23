def mari(a):
    x = 2
    while True:
        y = (x + a/x) / 2
        if y == x:
            x = int(x)
            print(x)
            break
        x = y
        
    
mari(900)