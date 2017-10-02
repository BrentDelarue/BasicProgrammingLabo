#Getalformaten
type1 = input("Geef hier het te vertalen getalformaat in: ")
type2 = input("Geef hier het te bekomen getalformaat in: ")
getal = float(input("Geef hier het te vertalen getal in: "))
if type1 != ("Binair", "binair", "octaal", "Octaal", "Decimaal", "decimaal", "Hexadecimaal", "hexadecimaal"):
    print("Het eerste opgegeven getalformaat wordt niet ondersteund.")
elif type2 != ["Binair", "binair", "octaal", "Octaal", "Decimaal", "decimaal", "Hexadecimaal", "hexadecimaal"]:
    print("Het tweede opgegeven getalformaat wordt niet ondersteund.")
elif type1 == type2:
    print("De opgegeven getalformaten zijn identiek.")
else:
    if type1 == ["Binair", "binair"]:
        if type2 == ["Decimaal", "decimaal"]:
            pass
    elif type1 == ["Binair", "binair"]:
        if type2 == ["Octaal", "octaal"]:
            pass
    elif type1 == ["Binair", "binair"]:
        if type2 == ["Hexadecimaal", "hexadecimaal"]:
            pass
    elif type1 == ["Decimaal", "decimaal"]:
        if type2 == ["Binair", "binair"]:
            rest = getal % int(getal)
            newgetal = int(getal - rest)
            binair = ""
            binair2 = ""
            while newgetal > 0:
                newgetalrest = newgetal % 2
                newgetal -= newgetalrest
                newgetal = int(newgetal / 2)
                binair += str(newgetalrest)
            while rest != 0:
                rest = rest * 2
                if rest < 1:
                    binair2 += "0"
                else:
                    binair2 += "1"
                    rest = rest - 1

                def rev(binair):
                    return binair[::-1]
                binair = rev(binair)
            print("Het decimale getal was: {}, het bekomen binaire getal is {},{}".format(getal, binair, binair2))
    elif type1 == ["Decimaal", "decimaal"]:
        if type2 == ["octaal", "Octaal"]:
            pass
    elif type1 == ["Decimaal", "Decimaal"]:
        if type2 == ["Hexadecimaal", "hexadecimaal"]:
            pass
    elif type1 == ["octaal", "Octaal"]:
        if type2 == ["Decimaal", "decimaal"]:
            pass
    elif type1 == ["Octaal", "octaal"]:
        if type2 == ["binair", "Binair"]:
            pass
    elif type1 == ["Octaal", "octaal"]:
        if type2 == ["Hexadecimaal", "hexadecimaal"]:
            pass
    elif type1 == ["Hexadecimaal", "hexadecimaal"]:
        if type2 == ["Decimaal", "decimaal"]:
            pass
    elif type1 == ["Hexadecimaal", "hexadecimaal"]:
        if type2 == ["Binair", "binair"]:
            pass
    elif type1 == ["Hexadecimaal", "hexadecimaal"]:
        if type2 == ["octaal", "Octaal"]:
            pass
