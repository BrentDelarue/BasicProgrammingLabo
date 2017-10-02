#oef3
import math
def maximum(a,b,c):
    if (a>b):
        if (a>c):
            print("{} is het grootste getal.".format(a))
        else:
            print("{} is het grootste getal.".format(c))
    elif (b>c):
        print("{} is het grootste getal.".format(b))
    else:
        print("{} is het grootste getal.".format(c))
a = int(input("Geef het eerste getal op: "))
b = int(input("Geef het tweede getal op: "))
c = int(input("Geef het derde getal op: "))
maximum(a,b,c)
