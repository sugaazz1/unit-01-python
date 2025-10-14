"""
Exercise 1:
Write a Python program that prints the current date and time using the datetime module.
"""
print("---Task 1---")
print()
from datetime import datetime
 
day_time = datetime.now()#datetime.now prints the current day and time.

print(day_time)#The print allows you to see it.


"""
Exercise 2:
Write a Python program that prints the current date and time using the datetime module.
Using the strftime function format the date in standard U.S. date format (MM/DD/YYYY)
"""
print("---Task 2---")
print()
from datetime import datetime
current = datetime.now()
current2 = current.strftime("%m/%d/%Y")

print(current2)

"""
Exercise 3:
Using the strptime function, convert two strings into dates.
Then find the difference in days between the two.
"""
print("---Task 3---")
print()
check1 = "10/14/2025"
check2 = "10/17/2025"

checked1 = datetime.strptime(check1, "%m/%d/%Y")

checked2 = datetime.strptime(check2, "%m/%d/%Y")
print(checked1)
print(checked2)
checked3 = checked2 - checked1
print(checked3)

"""
Excercise 4:
Write a program that asks the user for their birthdate and calculates their current 
age using the datetime module.
"""
print("---Task 4---")
print()
birth = input("When is your birthday to find your current age? (m/d/Y)")

birthed = datetime.strptime(birth, "%m/%d/%Y")
birthed2 = datetime.now() - birthed
birthed3 = birthed2.days//365

print("You are", birthed3, "years old.")