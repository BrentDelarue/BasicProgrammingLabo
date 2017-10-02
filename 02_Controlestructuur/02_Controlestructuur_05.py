#oef5
score = float(input("Geef uw score op: "))
komma = score % int(score)
if (komma >= 0.5):
    score = int(score) + 1
else:
    score = int(score)
if (score <= 9.5):
    print("U bent gebuisd, volgende keer beter. Uw score werd gecorrigeerd naar {}.".format(score))
else:
    print("U bent geslaagd. Uw score werd gecorrigeerd naar {}.".format(score))