def print_rectangle(a,b,c):
    print(a)
    print("x" * a)
    print(f'x{(a-2)*" "}x')
    print(f'x{(a-2)*" "}x')
    print("x" * a)
    
    print(b)
    print("x" * b)
    print(f'x{(b-2)*" "}x')
    print(f'x{(b-2)*" "}x')
    print("x" * b)
    
    print(c)
    print("x" * c)
    print(f'x{(c-2)*" "}x')
    print(f'x{(c-2)*" "}x')
    print("x" * c)
    
a,b,c = map(int, input().split( ))
print_rectangle(a,b,c)