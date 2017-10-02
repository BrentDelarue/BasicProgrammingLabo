#oef3
jaar = int(input("Geef je geboortejaar op: "))
import datetime
nu = datetime.year
leeftijd = nu - jaar
if (leeftijd >= 18):
    print("Ubent nu {} jaar oud.".format(nu-jaar))
else:
