cont_book = {}

while True:#Everything is under a While loop so it runs forever instead of rewriting the code.

    print("Contact Book Menu:")
    print("1. Add Contact")
    print("2. Delete Contact")
    print("3. List Contacts")
    print("4. Exit")

    cont = int(input("Enter your choice: "))#cont= contact
    if cont > 4 or cont < 0:#If a user enters a choice more than the given, it loops and asks them to enter a valid choice number.
        print("Please enter a valid choice")
        print()
    elif cont == 1:
        cont_name = input("Enter contact name: ")
        cont_num = input("Enter the contacts phone number(phone number only): ")
        if not cont_num.isdigit() or len(cont_num) > 10: #This code basically checks if the user enters an actual number, and if it's less than 10 digits.
            #it it doesn't come to agreement to the conditional statments, the following is printed.
            print("Enter a number no more than 10 digits.")
        else:
            cont_book[cont_name] = cont_num
            print("Contact successfully added.")#Otherwise, if everything is in agreement with the conditional statement, the contact will be added successfully.
        print()
    elif cont == 2:
        cont_del = input("Which contact would you like to delete? ")
        if cont_del in cont_book:#This code checks if the user input is in the list of contacts.
            del cont_book[cont_del]#It deletes the contact if it's in the list.
            print("Contact successfully deleted.")
        else:
            print("Contact doesn't exist.")#If the user input for the contact they want to delete isn't in the contact list, the following is printed.
        print()
    elif cont == 3: 
        print("Contacts:")
        for x in cont_book:
            print(x, ":", cont_book[x])#The for loop code prints out the list of contacts without the dictionary symbols. For example, the curly brackets{}
        print()
    elif cont == 4:
        cont_exit = input("Are you sure?")
        if cont_exit.lower() == "yes":
            break#If the user chooses to exit, the code breaks/stops looping.
        print()

