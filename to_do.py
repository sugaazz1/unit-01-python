with open("todo.txt", "w+") as file:
     my_list = file.read()


print("Welcome to your To Do list. ")
print()
while True:
    ins_todo = input("Would you like to add, remove, clear all or exit: ")
    if ins_todo.lower() == "add":
        todo_list = input("What would you like to add: ")
        print()
        with open("todo.txt", "a") as file:
           file.write(todo_list+"\n")
        #my_list.append(todo_list)
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
    elif ins_todo.lower() == "exit":
         with open("todo.txt") as file:
              my_list = file.read()
              break