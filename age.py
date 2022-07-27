
from datetime import date

current_year = date.today().year
birth_year = input("Enter your birth year: ")

if not len(birth_year) == 4:
    print ("Please enter year in full format")
    quit()

age = current_year - int(birth_year)
if age <= 45:
    print("You are " + str(age) + " years old! ")
else:
    print("You are " + str(age) + " years old! Don't forget to take your pills")

