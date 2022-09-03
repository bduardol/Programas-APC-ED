from collections import deque
x=0
        
def duplicatas1(n):
    x=0
    stack = deque()
    for i in range(len(n)):
        if n[i] != ')':
            stack.append(n[i])
        else:
            if stack[-1] == '(' and n[i-1] != '(':
                x = 1
                return x
            while stack[-1] != '(':
                stack.pop()
            stack.pop()
    return x
def duplicatas2(n):
    x=0
    stack = deque()
    for i in range(len(n)):
        if n[i] != ']':
            stack.append(n[i])
        else:
            if stack[-1] == '[' and n[i-1] != '[':
                x = 1
                return x
            while stack[-1] != '[':
                stack.pop()
            stack.pop()
    return x
def duplicatas3(n):
    x=0
    stack = deque()
    for i in range(len(n)):
        if n[i] != '}':
            stack.append(n[i])
        else:
            if stack[-1] == '{' and n[i-1] != '{':
                x = 1
                return x
            while stack[-1] != '{':
                stack.pop()
            stack.pop()
    return x
    
qnt = int(input())


while qnt != 0:
    qnt -= 1
    expre = input()
    p = duplicatas1(expre)
    a = duplicatas2(expre)
    f = duplicatas3(expre)
    
    if p == 1 or a == 1 or f ==1:
	    print('A expressão possui duplicata.')
else:
	    print('A expressão não possui duplicata.')
	    

