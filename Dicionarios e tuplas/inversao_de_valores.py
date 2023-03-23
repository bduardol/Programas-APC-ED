dici={}
def inversao(dici):
    print(dici)
    dici = {v: k for k, v in dici.items()}
    print(dici)

for i in range(5):
    n=input()
    dici[n]=int(input())

inversao(dici)






