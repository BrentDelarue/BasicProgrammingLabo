#Xtra2
def stopafstand(snelheid, wegtoestand):
        snelheid = snelheid/3.6
        if (wegtoestand == "nat"):
            afstand = (snelheid*1)+((snelheid*snelheid)/(2*5))
        else:
            afstand = (snelheid*1)+((snelheid*snelheid)/(2*8))
        print("Uw stopafstand indien het wegdek {0} is bedraagd {1: 0.2f}m.".format(wegtoestand,afstand))
snelheid = int(input("Geef de snelheid op die u rijdt: "))
wegtoestand = input("Geef de toestand van het wegdek op(nat of droog): ")
stopafstand(snelheid, wegtoestand)