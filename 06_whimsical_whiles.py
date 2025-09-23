"""
1. Simple Counter:
Write a program that uses a while loop to print numbers from 1 to 10.
"""
print("---Task 1---")

i = 1
while i < 11:
    print(i)
    if i == 10:
#The loops breaks when i==10. As i originally equals 1, the code i += 1 adds one to the original i everytime the code loops, it keeps adding one until the conditions (if i ==10) is met, then it breaks.
        break
    i += 1


"""
2. Countdown:
Write a program that uses a while loop to print numbers from 10 to 1 in descending order.
"""
print("---Task 2---")
i = 11
#Similar scenaria here, but instead the loop breaks by itself when i is less than 1. If not, the loop will just keep subtracting into the negatives.
while i > 1:
    i -= 1
    print(i)


"""
3. Factorial Calculation:
Write a program that calculates the factorial of a given number using a while loop.
"""
print("---Task 3---")

fact_input = int(input("Enter a number for the factorial result: "))
#the fact_input variable stores the input for the factorial.
result = 1 

while fact_input > 0:
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
#first create a variable to store the password and the input.
while pass1 != passd:
    print("Incorrect password, try again")
    pass1 = input("Enter the password:")
#I put the variable for the input so that when the user tries to guess the password and they fail, it'll allow them to try again.
else:
    print("Correct Password")




"""
5. Sum of Digits:
Write a program that calculates the sum of the digits of a given number using a while loop.
"""
print("---Task 5---")

"""
6. Fibonacci Series:
Write a program that prints the first n numbers in the Fibonacci sequence using a while loop.
"""
print("---Task 6---")

n = int(input("Enter the numbe of Fibonacci sequence you would like to print: "))
#I used n as the variable to match the instructions.
begin = 0

fst_fibnum = 0
snd_fibnum = 1
#The first fibonaccie sequence starts with a 0 then a 1 as it adds the previous results to the new one.

while n > 0: 
    print(fst_fibnum)
    
    result = fst_fibnum + snd_fibnum
    
    fst_fibnum = snd_fibnum
    snd_fibnum = result
#This 2 fst_fibnum and snd_fibnum basically changes the roles of it. For example once the previous number is stalled, it's then added to the second number by these codes, fst_fibnum = snd_fibnum, snd_fibnum = result so that the previous result is added to the next one.
    snd_fibnum = result 
    n-=1
else:
    print("Enter a vaild number: ")
#if a valid number isn't inputed, then it tells them that.