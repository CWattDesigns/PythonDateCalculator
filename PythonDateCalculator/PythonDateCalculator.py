import datetime
import calendar 

#Prompts the user for their name and greets them
name = str(input("Enter your name: "))
print("Nice to meet you, " + name + "!\n")

#Prompts the user for their birthday
birthday = str(input("Enter your birthday (DD/MM/YYYY Format): "))

#Finds the day of the week the user's birthday occurred on
def findDay(birthday):
    born = datetime.datetime.strptime(birthday, '%d/%m/%Y').weekday()
    return (calendar.day_name[born])

#Outputs what day of the week the user was born on
print("\nYou were born on a " + findDay(birthday) + "!")
