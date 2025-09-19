name = input("What's your name? ")

pass1 = input(f"{name} do you have a pass? ")
#I made a variable to store the name input, as well as the input that ask whether u have a pass or not.


if pass1.lower() == "yes":
    time_pass = int(input("What time was it issued? "))
#Made a variable to ask what time the pass was given
    time_pass2 = int(input("What time is it now? "))
#made another variable to ask what time is it now.
    location = input(f"{name} where are you headed? ")
#to ask where the student was headed.
    
    if time_pass2 - time_pass <= 2:
        if location.lower() == "nurse" or location.lower()== "bathroom" or location.lower()== "office":
            print("You may go.")
#This conditional statement checked if the student wanted to go to one of these 3 locations. And if it was less than 2 hours that the time had passed. If true, then it prints you may go.
        else:
            print("You can't go there with this pass.")
    elif time_pass2 - time_pass > 2:
        print(f"{name} your pass is too old, go back to class or get a new pass.")
#This conditional statement checked if it's more than 2 hours, then she has to head back to class.
else:
    print(f"{name} you don't have a pass, get back to class. Or go ask for one.")
#This goes back to the original if statement, if the answer is "no", then it comes to this else statement.