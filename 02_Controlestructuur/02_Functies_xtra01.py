#Xtra1
def schrikkeljaar(jaar):
    if (jaar%4 == 0 and jaar%100 == 0 and jaar%400 == 0):
        print("{} is een schrikkeljaar.".format(jaar))
    if (jaar%4 == 0 and jaar%100 == 0 and jaar%400 != 0):
        print("{} is geen schrikkeljaar.".format(jaar))
    if (jaar%4 == 0 and jaar%100 != 0 and jaar%400 != 0):
        print("{} is een schrikkeljaar.".format(jaar))
    if (jaar%4 != 0):
        print("{} is geen schrikkeljaar.".format(jaar))
jaar = int(input("Geef een jaartal op: "))
schrikkeljaar(jaar)
