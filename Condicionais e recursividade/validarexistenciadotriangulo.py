def valid_triangle(a,b,c):
    l1= b-c
    if l1 < 0:
        l1 = l1* -1
    l2= a-c
    if l2 < 0:
        l2 = l2* -1
    l3= a-b
    if l3 < 0:
        l3 = l3* -1
    l11= b+c
    l22= a+c
    l33= a+b
    if (l1 < a < l11) and (l2 < b < l22) and (l33 < c < l33):
        print('valido')    
    else:
        print('invalido')
        
valid_triangle(5,10,9)
    