#oef3
jaar = int(input("Geef je geboortejaar op: "))
import datetime
leeftijd = datetime.datetime.now().year - jaar
if (leeftijd >= 18):
    print("U bent nu {} jaar oud, en oud genoeg.".format(leeftijd))
else:
    print("U bent nnu {} jaar oud, en nog niet oud genoeg.".format(leeftijd))