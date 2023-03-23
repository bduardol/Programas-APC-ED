import math

def TwoDSpace(deslocamento, amplitude, espaço):
    dicionario ={}
    for i in range(40):
        for j in range(40):
            dicionario[(i, j)] = 0
    for i in range(40):
            j = int(deslocamento - amplitude*math.sin(10*i*math.pi/180))
            dicionario[(j, i)] = "*"

    for i in range(20):
        x=1
        for j in range(40):
            if j==39:
                if dicionario[(i, j)] == 0:
                    print(f"{espaço}")
                else:
                    print(f"{dicionario[(i, j)]}")
                
            elif dicionario[(i, j)] == 0:
                print(f"{espaço}",end="")
            else:
                print(f"{dicionario[(i, j)]}",end="")
    
TwoDSpace(10, 8, "'")

