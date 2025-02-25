
print("What month is it?")

month = int(input("Write a number corresponding to the month from 1-12"))

mensaje1 = "The current season is Spring."
mensaje2 = "The current season is Summer."
mensaje3 = "The current season is Fall."
mensaje4 = "The current season is Winter."

seasonSpring = 3, 4, 5
seasonSummer = 6, 7, 8
seasonFall = 9, 10, 11
seasonWinter = 12, 1, 2

if month == 3:
    print(mensaje1)
elif month == 4:
    print(mensaje1)
elif month == 5:
    print(mensaje1)
elif month == 6:
    print(mensaje2)
elif month == 7:
    print(mensaje2)
elif month == 8:
    print(mensaje2)
elif month == 9:
    print(mensaje3)
elif month == 10:
    print(mensaje3)
elif month == 11:
    print(mensaje3)
elif month == 12:
    print(mensaje4)
elif month == 1:
    print(mensaje4)
elif month == 2:
    print(mensaje4)
else:
    print("Please enter a valid number from 1-12")

mensajeUnico = ("The month is")
