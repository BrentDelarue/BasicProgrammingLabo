#oef4
seconds = int(input("Give the number of seconds: "))
Seconds = seconds%60
Minutes = int((seconds-Seconds)/60%60)
Hours =  int((seconds-Seconds-Minutes)/60/60%24)
Days = int((seconds-Seconds-Minutes-Hours)/60/60/24)
print("d:h:m:s: ->  {}:{}:{}:{}".format(Days, Hours, Minutes, Seconds))