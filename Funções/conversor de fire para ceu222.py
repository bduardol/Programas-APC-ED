###def converte(fire):
   # fire = (fire-32)/1.8
    #fire = ('{:.1f}'.format(fire))

#a = converte(0.0)
#print(a)###

def converte(fire):
    fire = (fire-32)/1.8
    return('{:.1f}'.format(fire))
    
a = converte(float(input()))
print(a)