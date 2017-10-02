#oef2
c = 0
d = 0
def bewerking(a,b,c,d):
    uitkomst = a-b+c+-d
    print("{}-{}+{}-{}={}.".format(a,b,c,d,uitkomst))
a = int(input("Geef een eerste getal op: "))
b = int(input("Geef een tweede getal op: "))
c = int(input("Geef een derde getal op: "))
d = int(input("Geef een vierde getal op: "))
bewerking(a,b,c,d)
bewerking(b,c,d,a)
bewerking(a,b,0,0)