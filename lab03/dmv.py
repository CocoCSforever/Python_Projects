import random

fullname=input("Welcome to the DMV (estimated wait time is 3 hours)\nPlease enter your first, middle, and last name:\n")
name_break = fullname.rfind(' ')
firstname=fullname[:name_break]
lastname=fullname[name_break+1:]

birth_date=input("Enter date of birth (MM/DD/YY):\n")

date_break=birth_date.rfind('/')
expdate=birth_date[:date_break]+"/21"

number=''
for x in range(7):
    number = number+str(random.randint(0, 9))

print(f"-------------------------------------\nWashington Driver License\nDL "+number+f"\nLN {lastname}\nFN {firstname}\nDOB {birth_date}\nEXP {expdate}\n-------------------------------------")
