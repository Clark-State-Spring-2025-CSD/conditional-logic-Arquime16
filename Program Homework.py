
print("What month is it?")

month = int(input("Write a number corresponding to the month from 1-12"))

My_months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
nameMonth = len(My_months)

mensaje1 = "The current season is Spring."
mensaje2 = "The current season is Summer."
mensaje3 = "The current season is Fall."
mensaje4 = "The current season is Winter."

seasonSpring = 3, 4, 5
seasonSummer = 6, 7, 8
seasonFall = 9, 10, 11
seasonWinter = 12, 1, 2

if mensaje1 == 3:
    print(mensaje1)
elif mensaje1 == 4:
    print(mensaje1)
elif mensaje1 == 5:
    print(mensaje1)
elif mensaje2 == 6:
    print(mensaje2)
elif mensaje2 == 7:
    print(mensaje2)
elif mensaje2 == 8:
    print(mensaje2)
elif mensaje3 == 9:
    print(mensaje3)
elif mensaje3 == 10:
    print(mensaje3)
elif mensaje3 == 11:
    print(mensaje3)
elif mensaje4 == 12:
    print(mensaje4)
elif mensaje4 == 1:
    print(mensaje4)
elif mensaje4 == 2:
    print(mensaje4)
pass

mensajeUnico = ("The month is")

if __name__ == '__main__':
    print(f"{mensajeUnico} {My_months[month-1]} and {mensaje1, mensaje2, mensaje3, mensaje4}")
    

    