#Getalformaten
type1 = input("Geef hier het te vertalen getalformaat in: ")
type2 = input("Geef hier het te bekomen getalformaat in: ")
getal = float(input("Geef hier het te vertalen getal in: "))
if (type1 != "Binair" or type1 != "binair" or type1 != "octaal" or type1 != "Octaal" or type1 != "Decimaal" or type1 != "decimaal" or type1 != "Hexadecimaal" or type1 != "hexadecimaal"):
    print("Het eerste opgegeven getalformaat wordt niet ondersteund.")
if (type2 != "Binair" or type2 != "binair" or type2 != "octaal" or type2 != "Octaal" or type2 != "Decimaal" or type2 != "decimaal" or type2 != "Hexadecimaal" or type2 != "hexadecimaal"):
    print("Het tweede opgegeven getalformaat wordt niet ondersteund.")
if type1 == type2:
    print("De opgegeven getalformaten zijn identiek.")
else:
    if type1 == ["Binair" or "binair"]:
        if type2 == ["Decimaal" or "decimaal"]:
            pass
    elif type1 == ["Binair" or "binair"]:
        if type2 == ["Octaal" or "octaal"]:
            pass
    elif type1 == ["Binair" or "binair"]:
        if type2 == ["Hexadecimaal" or "hexadecimaal"]:
            pass
    elif type1 == ["Decimaal" or "decimaal"]:
        if type2 == ["Binair" or "binair"]:
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
    elif type1 == ["Decimaal" or "decimaal"]:
        if type2 == ["octaal" or "Octaal"]:
            pass
    elif type1 == ["Decimaal" or "Decimaal"]:
        if type2 == ["Hexadecimaal" or "hexadecimaal"]:
            pass
    elif type1 == ["octaal" or "Octaal"]:
        if type2 == ["Decimaal" or "decimaal"]:
            pass
    elif type1 == ["Octaal" or "octaal"]:
        if type2 == ["binair" or "Binair"]:
            pass
    elif type1 == ["Octaal" or "octaal"]:
        if type2 == ["Hexadecimaal" or "hexadecimaal"]:
            pass
    elif type1 == ["Hexadecimaal" or "hexadecimaal"]:
        if type2 == ["Decimaal" or "decimaal"]:
            pass
    elif type1 == ["Hexadecimaal" or "hexadecimaal"]:
        if type2 == ["Binair" or "binair"]:
            pass
    elif type1 == ["Hexadecimaal" or "hexadecimaal"]:
        if type2 == ["octaal" or "Octaal"]:
            pass
