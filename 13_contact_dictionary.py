cont_book = {}

while True:

    print("Contact Book Menu:")
    print("1. Add Contact")
    print("2. Delete Contact")
    print("3. List Contacts")
    print("4. Exit")

    cont = int(input("Enter your choice: "))
    if cont > 4:
        print("Please enter a valid choice")
    elif cont == 1:
        cont_name = input("Enter contact name: ")
        cont_num = input("Enter the contacts phone number(phone number only): ")
        if not cont_num.isdigit() or len(cont_num) > 10:
            print("Enter a number no more than 10 digits.")
        else:
            cont_book[cont_name] = cont_num
            print("Contact successfully added.")
        print()
    elif cont == 2:
        cont_del = input("Which contact would you like to delete? ")
        if cont_del in cont_book:
            del cont_book[cont_del]
            print("Contact successfully deleted.")
        else:
            print("Contact doesn't exist.")
        print()
    elif cont == 3: 
        print("Contacts:")
        for x in cont_book:
            print(x, ":", cont_book[x])
        print()
    elif cont == 4:
        cont_exit = input("Are you sure?")
        if cont_exit.lower() == "yes":
            break
        print()

