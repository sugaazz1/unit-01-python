import math

print("Welcome to the Calculator-inator 9000!")

fst_num = float(input("Enter the first number: "))
snd_num = float(input("Enter the second number:"))
#created 2 variable to store the inputs for the first and second number.
print("Select an Operation")
print()
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")
print("5. Floor Division")
print("6. Exponential")
print("7. Remainder")
#I made 7 prints statement to represent the 7 choices of operations.

choice = int(input("Enter choice: "))
if choice > 0 :
    if choice == 1:
        print("Result:", fst_num + snd_num)
    elif choice == 2:
        print("Result:", fst_num - snd_num)
    elif choice == 3:
        print("Result:", fst_num * snd_num)
    elif choice == 4:
#for the division, I made an if statement to check if the user put in a zero for the second number. As you can't divide by the number zero.
        if snd_num == 0:
            print("Can't divide by zero")
        result = fst_num / snd_num
        print("Result: {0:.2f}".format(result))
    elif choice == 5: 
        result = fst_num // snd_num
        print("Result:", result)
    elif choice == 6:
        result = fst_num ** snd_num
        print("Result: {0:.2f}".format(result))
#For choices 6 and 7, i rounded both their result outs to 2 digits after the decimal number. If not it would just go on and on, and eventually say overload.
    elif choice == 7:
        result = fst_num % snd_num
        print("Result: {0:.2f}".format(result))
    elif choice > 7:
        print("Input a correct choice.")
#Lastly, I made an elif to see if the user puts in a choice that's not between 1-7. If they chose a number like 10, it'll print, that's not a valid choice number.
else:
    print("Enter a valid choice.")
#Similar to choice > 7, this else statement check is the user puts in -numbers as their choice or letters, then says choose a valid choice number.






#addition = fst_num + snd_num
#subtraction = fst_num - snd_num
#multiplicaiton = fst_num * snd_num
#division = fst_num / snd_num
#floor_division = fst_num // snd_num
