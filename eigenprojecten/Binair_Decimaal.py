# binair naar decimaal
import sys
getal = input("Geef een binair getal op: ")
element = "0"
waarde1 = 0
waarde2 = 0
waarde4 = 0
geheelgetal = 0
decimaalgetal = 0.0
while element != ",":
    if getal[waarde1:waarde1+1] != ",":
        element = getal[waarde1:waarde1+1]
        waarde1 += 1
    else:
        element = getal[waarde1:waarde1+1]
geheel = getal[:waarde1]
decimaal = getal[(waarde1+1):]
while waarde2 != waarde1+1:
    waarde3 = waarde1
    geh = float(getal[waarde2:waarde2+1])
    geh = geh*(2**waarde3)
    geheelgetal += geh
    waarde3 -= 1
    waarde2 += 1
maximaal = sys.getsizeof(getal[waarde1+1:])
while waarde4 != maximaal+1:
    dec = float(getal[waarde4:waarde4+1])
    dec = dec*(2**(-(waarde4+1)))
    decimaalgetal += dec
    waarde4 += 1
totaal = float(geheelgetal)+decimaalgetal
print("Het opgegeven binair getal was {}, het equivalent decimaal getal is {}.".format(getal, totaal))
