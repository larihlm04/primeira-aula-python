assento = input("Digite o assento: ").lower()

letra = assento[0].upper()

if letra == "A" or letra == "E" or letra == "I" or letra == "O" or letra == "U":
    print("Assento Premium")

else:
    print("Assento Regular")