"""
Task 1: Greeting
Write a function that takes a name as a 
agrument and prints a greeting message like "Hello, [name]!".
"""
print("---Task 1---")

def greetings(name):
    """

    """
    print("Hello " + name)
greetings("Mingle")
print()
"""
Task 2: Square of a Number
Write a function that takes an integer as an argument and returns its square.
"""
print("---Task 2---")

def exponents(a,b):
    """
    """
    return a ** b#To square root a number, you use 2 asteriks *. 

print(exponents(3,5))#3 in this scenario, is being raised to the power of 5.
print()
"""
Task 3: Even or Odd
Write a function that takes a number as a argument that 
returns `True` if the number is even, and `False` otherwise.
"""
print("---Task 3---")

def test(a):
    """
    """
    return a % 2 == 0 #the % sign is used to find numbers that have 0 remainder. It's saying that if a number is divisible by 2, it'll print true else print false.

print(test(9)) #Since 9 isn't divisible by 2, It'll print false.


print()
"""
Task 4: Area of a Rectangle
Write a function that takes the length and width of a rectangle and returns its area.
"""
print("---Task 4---")

def area(c,d):
    """
    """
    return c*d #This code multiples the given number by the second given number to find the area.
print(area(4,9))#The length is 4, and the w is 9.

print()
"""
Task 5: Celsius to Fahrenheit
Write a function that takes a temperature in Celsius and returns 
the equivalent temperature in Fahrenheit using the correct formula
"""
print("---Task 5---")

def temp(e):
    """
    """
    return (e * 1.8) + 32
print(temp(23))


print()
"""
Task 6: Average of Numbers
Write a function that takes a list of numbers as an argument
and returns the average (mean) of those numbers.
"""
print("---Task 6---")


def num_ave(ave_num):
    return sum(ave_num) / len(ave_num)
print(num_ave([2,5,9,1,8,0,7,3,4,6]))

print()
"""
Task 7: Total Calculator
Create a function that has arguments for the price and quantity of something, 
and returns the total.

Your function should also optionally accept a 3rd argument for discount as a float, 
and return the discounted if provided.
"""
print("---Task 7---")

def store(p,q, discounts=0.0):

    subtotal = p *q
    return subtotal - (subtotal * discounts)

print(store(4,8,0.7))
