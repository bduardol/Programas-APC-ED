def anobissexto(x):
    if (x%4 == 0 and x%100 != 0) or (x%400 == 0):
        return "sim"
    else:
        return "não"

print(anobissexto(2100))