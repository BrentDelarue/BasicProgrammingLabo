#oef4
leeftijdH = int(input("Geef de leeftijd op van uw hond: "))
leeftijd = 22 + (leeftijdH - 2) * 5
if (leeftijdH <= 0):
    print("Een probleem, uw hond is nog niet geboren.")
elif (leeftijdH == 1):
    print("De leeftijd van uw hond in mensenjaren is 14 jaar.")
elif (leeftijdH == 2):
    print("De leeftijd van uw hond in mensenjaren is 22 jaar.")
else:
    print("De leeftijd van uw hond in mensenjaren is {} jaar.".format(leeftijd))