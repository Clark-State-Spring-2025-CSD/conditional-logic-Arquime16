
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

def get_season_message(month): 
    if month in seasonSpring:
        return mensaje1
    elif month in seasonSummer:
        return mensaje2
    elif month in seasonFall:
        return mensaje3
    elif month in seasonWinter:
        return mensaje4
    else:
        return "Invalid month"

mensajeUnico = ("The month is")

if __name__ == '__main__':
    print(f"{mensajeUnico} {My_months[month-1]} and {get_season_message(month)}")
    

    