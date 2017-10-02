# Labo 01  - basis variabelen ("#" = commentaar)

# print("Hello world, dag Brent")    #String= tekst
#                                    #print= methode, argumenten bevinden zich tussen ()
#                                    #1= integer, 1.0= double
# print('Hello world, dag Brent')    #''=""
# print("Hello world, \t dag Brent") #\= escape funtcie = speciale actie, \t= tab, \n= new line
# print("Hello world, \n dag Brent")

#oef1
naam = input("Geef mij jouw naam: ")#prompt= input =  een vraagstelling
voornaam = input("Geef mij uw voornaam: ")
leeftijd = input("Geef mij uw leeftijd: ")
#datatype conversie int, float ... = Leeftijd = int(leeftijd)
print("\nVoornaam: {0} \nAchternaam: {1} \nLeeftijd: {2}".format(voornaam , naam , leeftijd))#print("\nVoornaam: {0} \nAchternaam: {1}").format(voornaam , naam)format werkt niet na prints, wel op strings.
