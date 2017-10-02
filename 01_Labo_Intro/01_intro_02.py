komma = float(input("Geef een kommagetal: "))
getal = komma%int(komma)
newgetal = int(komma - getal)
binair = ""
binair2 = ""
while newgetal > 0:
    newgetalrest = int(newgetal % 2)
    newgetal -= newgetalrest
    newgetal = int(newgetal / 2)
    binair += str(newgetalrest)
while getal != 0:
    getal = getal * 2
    if getal < 1:
        binair2 += "0"
    else:
        binair2 += "1"
        getal -= 1
def rev(binair): return binair[::-1]
binair = rev(binair)
print("{},{}".format(binair, binair2))