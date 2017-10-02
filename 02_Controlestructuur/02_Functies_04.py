#oef4
def maand(maandnummer):
    if (maandnummer == 1):
        maand = "januari"
        print("De maand is {}.".format(maand))
    elif (maandnummer == 2):
        maand = "februari"
        print("De maand is {}.".format(maand))
    elif (maandnummer == 3):
        maand = "maart"
        print("De maand is {}.".format(maand))
    elif (maandnummer == 4):
        maand = "april"
        print("De maand is {}.".format(maand))
    elif (maandnummer == 5):
        maand = "mei"
        print("De maand is {}.".format(maand))
    elif (maandnummer == 6):
        maand = "juni"
        print("De maand is {}.".format(maand))
    elif (maandnummer == 7):
        maand = "juli"
        print("De maand is {}.".format(maand))
    elif (maandnummer == 8):
        maand = "augustus"
        print("De maand is {}.".format(maand))
    elif (maandnummer == 9):
        maand = "september"
        print("De maand is {}.".format(maand))
    elif (maandnummer == 10):
        maand = "oktober"
        print("De maand is {}.".format(maand))
    elif (maandnummer == 11):
        maand = "november"
        print("De maand is {}.".format(maand))
    elif (maandnummer == 12):
        maand = "december"
        print("De maand is {}.".format(maand))
    else:
        maand = "niet weer te geven"
        print("De maand is {}.".format(maand))
maandnummer = int(input("Geef een maandnummer in: "))
maand(maandnummer)