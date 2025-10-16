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
current2 = current.strftime("%m/%d/%Y")#This code prints out the current time in the date format that you want it in. 

print(current2)

"""
Exercise 3:
Using the strptime function, convert two strings into dates.
Then find the difference in days between the two.
"""
print("---Task 3---")
print()
check1 = "10/14/2025"
check2 = "10/17/2025"#These two variable stores 2 different dates.

checked1 = datetime.strptime(check1, "%m/%d/%Y")
#The strptime function takes the date from the variable the string is stored in, and converts it to actual date. As long as they are in the same format.
checked2 = datetime.strptime(check2, "%m/%d/%Y")

print(checked1)
print(checked2)
checked3 = checked2 - checked1
#To check the difference in days between the 2 dates, you apparenlty just put a subtraction sign, and the computer does the rest.
print(checked3)

"""
Excercise 4:
Write a program that asks the user for their birthdate and calculates their current 
age using the datetime module.
"""
print("---Task 4---")
print()
birth = input("When is your birthday to find your current age? (m/d/Y)")#ask users for their input.

birthed = datetime.strptime(birth, "%m/%d/%Y")#This code takes the users birthday input and formats it for the computer to do come actual calculations with.
birthed2 = datetime.now() - birthed #This code subtracts your birthday from the current day.
birthed3 = birthed2.days//365 #The code by default tells you the difference in days. So we divide the days by 365 to get the years

print("You are", birthed3, "years old.")