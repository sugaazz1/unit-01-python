'''
Exercise 1:
Check if an integer is even and greater than 10.
Return True if both conditions are met, False otherwise.
'''
print("--Task 1---")

even_greater = int(input("Insert an interger: "))
#I made a variable to store the input, and added to the int() syntax so the input only takes an interger.
if even_greater > 10 and even_greater % 2==0:
    print("True") 
#I made an if statement per the Exercist request. I also the if statement so that if its even, and is greater than 10, it prints true.
else:
    print("False")
#If one or both of the conditions are not met, then it prints false.

'''
Exercise 2:
Determine the ticket price based on age and student status.
Price is $10 if under 18 or a student, $20 otherwise.
'''
print("--Task 2---")

student_age = int(input("How old are you: "))
student_status = input("What's your status: ")
# I made 2 variables to store the input that asks for age and the other one that asks for you status.
if student_age < 18 or student_status.lower() == "student" :
    print("$10 please")
# Using what we learned today in class, I made a conditional statment saying if applicant is under 18 OR a student they pay $10.
else:
    print("$20 please")
#The else statment is for anyone that is over 18 and is not a student


'''
Exercise 3:
Prompt the user to enter a fruit name. Check if the fruit is in the list. 
If it is, print "Yes, that fruit is in the list." 
If it's not, print "No, that fruit is not in the list."
'''
print("--Task 3---")

list_of_fruits = ["apple", "banana", "orange", "grape", "pineapple", "mango", "kiwi", "strawberry", "blueberry", "raspberry",
    "blackberry", "watermelon", "cantaloupe", "honeydew", "papaya", "pear", "peach", "plum", "nectarine",
    "apricot", "cherry", "lime", "lemon", "pomegranate", "grapefruit", "passionfruit", "dragonfruit",
    "guava", "fig", "date", "lychee", "tangerine", "coconut", "jackfruit", "durian", "starfruit", "persimmon",
    "cranberry", "boysenberry", "gooseberry", "mulberry", "sapodilla", "tamarind", "longan", "rambutan",
    "kumquat", "quince", "jabuticaba", "currant", "acerola", "miracle fruit", "salak", "physalis",
    "elderberry", "soursop", "breadfruit", "carambola", "bael", "chempedak", "pitaya", "mangosteen"]
#No I didn't type this all out, I copied and pasted the list of fruits.
fruits = str(input("Enter a fruit name: "))
#Made a variable to store the input for "Enter a fruit name:"
if fruits.lower() in list_of_fruits:
    print("Yes, that fruit is in the list.")
#I made a conditional statement that basically checked if the fruit the user entered was in the list above. If it wasn't, then it'll print, not in the list, if it is, it'll print it's in the list.
else:
    print("No, that fruit is not in the list.")


'''
Exercise 4:
Check if a year is a century year and a leap year.
'''
print("--Task 4---")




'''
Exercise 5:
Calculate the cost of shipping for an online order based on the order weight and destination zone. 
The shipping cost is $5 per kilogram for Zone A and $7 per kilogram for Zone B. 
If the order weight is less than 0 kg, return an error message.
'''
print("--Task 5---")




'''
Exercise 6:
Determine the type of a triangle based on side lengths.
Equilateral, Isosceles, Scalene, or Not a triangle.
'''
print("--Task 6---")

side1 = input("Enter a side length of one triangle: ")
side2 = input("Enter a 2nd side length: ")
side3 = input("Enter the 3rd side length: ")
#I made 3 variables to store 3 inputs that asks for the side lengths of a triangle.
if side1==side2==side3 :
    print("An Equilateral Triangle.")
elif side1==side2!=side3 or side1==side3!=side2 or side2==side3!=side1 or side2==side1!=side3 or side3==side2!=side1 or side3==side1!=side2 :
    print("An Isosceles Triangle.")
elif side1!=side2!=side3 :
    print("A Scalene Triangle.")
else:
    print("What are you doing?")
#After I made the variables, I had to make conditional statment so python would be able to associate which pattern of the side length represents an equilateral, isosceles, or a scalene triangle. 