"""
TASK 1:
Write code that checks if a user entered the correct password.
The password should not be case sensitive

"""
print("----Task 1----")
#Did task 1 so it would be easier to identify in the terminal.

password_insert = input("Enter a password:")
#I made a variable for my input so I can keep track of it.
if password_insert.lower() == "password":
#I made an if statement to let the user know if they entered the wrongor incorrect password. If they got it write a message will print "you have entered the correct password."
    print("you have entered the correct password")
else:
#I made an else statement incase they accidentally put the wrong password.
    print("INCORRECT PASSWORD")


"""
TASK 2:
Write code that checks if a user inputs an empty string
If the string is empty, print "invalid" otherwise print "valid"
"""
print("----Task 2----")

empty_string = str(input("Enter a series of String, or letters: "))
#I made a variable to store the input question.
if empty_string.strip() == "":
#Then I made an if statement to see if the user will leave the question empty or add a bunch of spaces. That's what the strip does, remove the unneccessary spaces.
    print("Invalid")
#I made it print invalid if the left it empty or added a bunch of spaces.
else: 
    print("Valid")
#AFter that, I made an else statment, basically saying that if they actually put letters, or words, print valid.




"""
TASK 3:

Write a program that will replace the word "cat" with the word "dog"
It should replace all occurances regardless of captilization 
"""
print("----Task 3----")

name= input("What's the best pet? Cat or Dog?:")
#I first made an input for the user to type in what the best pet is.
new_name = name.lower().replace("cat", "dog")
#For those who chooses the word cat, it will be changed to dog.
print(new_name)



"""
TASK 4:

Write a program that takes a person's name and age as input and prints it
"""
print("----Task 4----")

input_name = input("What's your name? ")
#I made a variable to store the input that asks for you name.
input_age = input("How old are you? ")
#Then I also did the same for the age, made a variable to store the age input.
name_age = input_name +" you're" + " " + input_age
#I created another variable that would add these two inputs together to form a sentence.
print (name_age, "years old.")
#Lastly I printed it and it worked.



"""
TASK 5:

Write a program that takes in two floats, and prints the quotient
The result should be rounded to the nearest tenth (1 decimal place)
"""
print("----Task 5----")


input1 = float(input("Insert a decimal or float number: "))
#As usual I made a variable to store the input. But I also added the float command so python only knows to take float numbers.
if input1.is_integer():
    print("Enter a valid decimal number")
else:
    print("")
#Then I made if else statement incase the user puts something that doesn't correlate with the code. I made it so that if they put an integer number, it'll print "Enter a valid decimal number."


input2 = float(input("Enter another decimal or float number: "))
#Similar to input1, I did the same thing over here.
if input2 == 0 :
    print("Cannot divide by zero")
elif input2.is_integer():
    print("Enter a decimal number.")
else:
    print("")
#I made if else statments in input2 as well. I also added the elif statment incase the user put a zero.

division = input1 // input2 
print("Division: ",division)
#Then I divide input1 and input2 by using 2 // which tells python to round up to the nearest tenth place.
