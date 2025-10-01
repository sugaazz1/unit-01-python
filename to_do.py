print("Welcom to your To Do list. ")
print()
my_list = []
while True:
    ins_todo = input("Would you like to add or remove a to do. Or clear all: ")
    if ins_todo.lower() == "add":
        todo_list = input("What would you like to add: ")
        print()
        my_list.append(todo_list)
        print()
        print("Your current to do list:")
        for i in my_list:
             print(i)

    elif ins_todo.lower() == "remove":
            todo_rem = int(input("What # to do would you like to remove: "))
            print()
            del my_list[todo_rem -1]
            print()
            print("Your current to do list:")
            for i in my_list:
                 print(i)
    elif ins_todo.lower() == "clear all":
            yes_clear = input("Are you sure? ")
            if yes_clear.lower() == "yes":
                my_list.clear()
                print("Your current to do list: ")
                print(my_list)
                for i in my_list:
                     print(i)
            else:
                 print()