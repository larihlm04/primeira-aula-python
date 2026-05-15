def ehpar(x):
    y = x % 2 == 0
    if y:
        return "Par"
    else:
        return "Impar"

a = ehpar(x=4)
print(a)
b = ehpar(x=7)
print(b)