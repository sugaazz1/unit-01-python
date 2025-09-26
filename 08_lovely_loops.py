print("Try to guess the password.")

username = input("Enter username: ")
lockout_threshold = int(input("Enter lockout threshold: "))
security_level = input("Enter security level. Low, Medium or High:")


attempts = 0
login_successful = False

if security_level.lower() == "low":
    password = "password"
    password_input = input("Guess the correct password:")
    while password_input != password:
        attempts += 1
        password_input = input("Guess the correct password:")
        if attempts == lockout_threshold:
            print("You've reached the maximum attempt.")
    else:
        print("Good job, you got it.")

elif security_level.lower() == "medium":
     password = "

elif security_level.lower() == "high":
    password = "supercalifragilisticexpialidocious"
    password_input = input("Guess the correct password:")
    while password_input != password:
        attempts += 1
        password_input = input("Guess the correct password:")
        if attempts == lockout_threshold:
            print("You've reached the maximum of attempts.")
    else: 
            print(f"Wow you actually got it {username} props to you nerdd.")


else:
   print("Enter a valid Security Level.")