name = input("What's your name? ")

pass1 = input(f"{name} do you have a pass? ")



if pass1.lower() == "yes":
    time_pass = int(input("What time was it issued? "))

    time_pass2 = int(input("What time is it now? "))

    location = input(f"{name} where are you headed? ")
    
    print(time_pass)
    print(time_pass2)
    if time_pass2 - time_pass <= 2:
        print(location)
        if location.lower() == "nurse" or location.lower()== "bathroom" or location.lower()== "office":
            print("You may go.")
        elif location.lower != "nurse" or location.lower() != "bathroom" or location.lower()!= "office":
            print("You can't go there with this pass.")
    elif time_pass2 - time_pass > 2:
        print(f"{name} your pass is too old, go back to class or get a new pass.")
    
else:
    print(f"{name} you don't have a pass, get back to pass.")