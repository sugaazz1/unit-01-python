print("Try to guess the password.")
#Title of the game/code.
username = input("Enter username: ")
lockout_threshold = int(input("Enter lockout threshold: "))
security_level = input("Enter security level. Low, Medium or High: ")
#Variable for the various inputs the user needs.

attempts = 0
login_successful = False

if security_level.lower() == "low":
    password = "password"
    password_input = input("Guess the correct password: ")
    while password_input != password:
        attempts += 1
        password_input = input("Incorrect, guess the correct password: ")
        if attempts == lockout_threshold:
#This code basically shows that if it's on their last try and they get it right, it'll let them know that they actually got it.
            if password_input == password:
                print("Lowkey Easy for real.")
            else:
                print("You've reached the maximum attempt.")
            break
    else:
#If they guess the password on the first try, this message pops up.
        print("Good job, you got it.")

elif security_level.lower() == "medium":
    password = "dictionaries"
    password_input = input("Guess the correct password: ")
    while password_input != password:
        attempts += 1
        password_input = input("Incorrect, guess the correct password: ")
        if attempts == lockout_threshold:
            if password_input == password:
                print("Nice you got on the very last try.")
            else:
#If the user gets to hte last attepmt and still didn't guess the password. I'll print the following statement below.
                print("You've reached the maximum attempt.")
            break
    else:
        print("You got it.")

elif security_level.lower() == "high":
    password = "supercalifragilisticexpialidocious"
    password_input = input("Guess the correct password: ")
    while password_input != password:
        attempts += 1
        password_input = input("Incorrect, guess the correct password: ")
#Putting the password input again serves to make sure that when the user guesses the password wrong, it'll give them the option to try and guess the password again.
        if attempts == lockout_threshold:
            if password_input == password:
                print(f"Crazy you guessed this {username}??")
            else:
                print("You've reached the maximum of attempts.")
            break
    else: 
#I put the format option to show the user that they're recognized for actually getting a word like this.
            print(f"Wow you actually got it {username} props to you nerdd.")


else:
   print("Enter a valid Security Level.")
#if the user enters anything other than the security level. It'll print the following statement.