""""
TASK 1:
Create a float variable, and then convert it to an integer
Print both the original variable and the converted integer.

"""

my_float = 6.7
#I first made a float variable using my_float.
my_int= int(my_float)
#After that I made my_int variable to change the float into an interger.
print("Original Float", my_float)
print("Interger", my_int)
#After doing that, I ran the code using print to see if it works, and it did.


"""
TASK 2:
Write code that takes a number as input and prints whether 
it's positive, negative, or zero using if-elif-else statements.
"""

input_number = int(input("Input a number to see if it's Negative, Positive, or Zero:"))
#I made an input so the user will be able to enter a number to see if it's positive negative or zero.
if input_number > 0:
        print("Positive")
#I made an if statement saying if the number is greater than zero, then it is Positive.
elif input_number < 0:
        print("Negative")
#Then I made an else if statement saying that if the number is less than zero, the user will see that it's negative.
else:
        print("Zero")
#and Lastly, anything that is not a number will be given zero.





"""
TASK 3:

Write code that takes two numbers as input (an integer and a float), 
performs addition, subtraction, multiplication, and division, and prints the results.
"""


"""
TASK 4:

Create a dictionary with keys as fruit names and values as their respective quantities. 
Then print out the quantity of one of the fruits.
"""


"""
TASK 5:

Create a string variable with that is a list of numbers and convert that string into a tuple.
Then print out the both the original string and tuple.
"""

"""
TASK 6:

Create a list of your favorite subjects (as strings). 
Use the join() function to combine all subjects into a single string separated by commas.
Then create another version using " - " as the separator.
Print both the original list and both joined strings.
"""