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

#empty_string = 




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




"""
TASK 5:

Write a program that takes in two floats, and prints the quotient
The result should be rounded to the nearest tenth (1 decimal place)
"""
print("----Task 5----")

