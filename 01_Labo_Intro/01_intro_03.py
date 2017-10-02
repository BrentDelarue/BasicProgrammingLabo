#oef3
days = int(input("Give the number of days: "))
hours = int(input("Give the number of hours: "))
minutes = int(input("Give the number of minutes: "))
seconds = int(input("Give the number of seconds: "))
time = (days*24*60*60) + (hours*60*60) + (minutes*60) + seconds
print("The total amount of seconds = {}.".format(time))