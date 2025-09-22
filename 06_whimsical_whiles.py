"""
1. Simple Counter:
Write a program that uses a while loop to print numbers from 1 to 10.
"""
print("---Task 1---")

i = 1
while i < 11:
    print(i)
    if i == 10:
        break
    i += 1


"""
2. Countdown:
Write a program that uses a while loop to print numbers from 10 to 1 in descending order.
"""
print("---Task 2---")
i = 11

while i > 1:
    i -= 1
    print(i)


"""
3. Factorial Calculation:
Write a program that calculates the factorial of a given number using a while loop.
"""
print("---Task 3---")

fact_input = int(input("Enter a number for the factorial result:"))
result = 1 

while fact_input > 0:
    #print(fact_input)
    result = fact_input * result
    fact_input -= 1
print(result)




"""
4. Password Guessing Game:
Create a simple password guessing game using a while loop. Ask the user to guess a predefined password and provide appropriate feedback.
"""
print("---Task 4---")

passd = "hotdogs"
pass1 = input("Enter the password:")

while pass1 != passd:
    print("Incorrect password, try again")
    pass1 = input("Enter the password:")
else:
    print("Correct Password")




"""
5. Sum of Digits:
Write a program that calculates the sum of the digits of a given number using a while loop.
"""
print("---Task 5---")

#number = int(input("Inser a number:"))

"""
6. Fibonacci Series:
Write a program that prints the first n numbers in the Fibonacci sequence using a while loop.
"""
print("---Task 6---")