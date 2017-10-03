#oef5
def geef_celsius(fahrenheit):
    temp = (fahrenheit-32)*5/9
    print("{}°F is {}°C.".format(fahrenheit,temp))
def geef_fahrenheit(celsius):
    temp = (celsius*9/5)+32
    print("{}°C is {}°F.".format(celsius,temp))
type = input("Welke eenheid gebruikt u? ")
if (type == "fahrenheit"):
    fahrenheit = float(input("Geef de graden in fahrenheit: "))
    geef_celsius(fahrenheit)
elif (type == "celsius"):
    celsius = float(input("Geef de graden in celsius: "))
    geef_fahrenheit(celsius)
else:
    print("De opgegeven eenheid wordt niet ondersteund.")