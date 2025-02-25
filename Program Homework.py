
print("What month is it?")

month = input("Write a number corresponding to the month from 1-12")

mensaje1 = "The current season is Spring."
mensaje2 = "The current season is Summer."
mensaje3 = "The current season is Fall."
mensaje4 = "The current season is Winter."

mensajeUnico = ("The month is")

if month == "january" is 1:
    print(mensajeUnico, "January")
elif month == "february" is 2:
    print(mensajeUnico, "february")         
elif month == "march" is 3:
    print(mensajeUnico, "March")
elif month == "april" is 4:
    print(mensajeUnico, "April")
elif month == "may" is 5:
    print(mensajeUnico, "May")
elif month == "june" is 6:
    print(mensajeUnico, "June")
elif month == "july" is 7:
    print(mensajeUnico, "July")
elif month == "august" is 8:
    print(mensajeUnico, "August")
elif month == "september" is 9:
    print(mensajeUnico, "September")
elif month == "october" is 10:
    print(mensajeUnico, "October")
elif month == "november" is 11:
    print(mensajeUnico, "November")
elif month == "december" is 12:
    print(mensajeUnico, "December")
else:
    print("Please enter a valid month")


if month == "3" or month == "4" or month == "5":
    print(mensaje1)
elif month == "6" or month == "7" or month == "8":
    print(mensaje2)
elif month == "9" or month == "10" or month == "11":
    print(mensaje3)
else:
    print(mensaje4)