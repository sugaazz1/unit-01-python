print("Try to guess the password.")
#Title of the game/code.
username = input("Enter username: ")
lockout_threshold = int(input("Enter lockout threshold: "))
security_level = input("Enter security level. Low, Medium or High: ")
#Variable for the various inputs the user needs.

attempts = 0
login_successful = False

while attempts < lockout_threshold:

    if security_level.lower() == "low":
        password_input = input("Guess the correct password: ")
        if password_input.lower() == "password":
            login_successful = True
            print("Login Successful!")
    #If they guess the password on the first try, this message pops up.

            break
        else:
            attempts += 1
            print("Incorrect password, Try again.")
            if attempts >= lockout_threshold:
                print("You've reached the maximum amount of attempt.")
                break

            

    elif security_level.lower() == "medium":
        password_input = input("Guess the correct password: ")
        if password_input.lower() == "dictionaries":
            login_successful = True
            print("Nicee you got it.")
            break
        else: 
            attempts += 1
            print("Incorrect password, try again.")
            if attempts >= lockout_threshold:
    #If the user gets to hte last attepmt and still didn't guess the password. I'll print the following statement below.
                    print("You've reached the maximum attempt.")
                    break

    elif security_level.lower() == "high":
        password_input = input("Guess the correct password: ")
        if password_input.lower() == "supercalifragilisticexpialidocious":
            login_successful = True
            print(f"Wow you actually got it {username} props to you nerdd.")
#I put the format option to show the user that they're recognized for actually getting a word like this.
            break
        else:
             attempts += 1 
             print("Incorrect password, try again.")
             if attempts >= lockout_threshold:
                    print("You've reached the maximum of attempts.")
                    break

    #I put the format option to show the user that they're recognized for actually getting a word like this.


    else:
        print("Enter a valid Security Level.")
    #if the user enters anything other than the security level. It'll print the following statement.