import random

"""
Task 1 (random module):
Write a program that simulates rolling a six-sided die 10 times.
Print each roll result.
"""
print("---Task 1---")
dice = [random.randrange(1,7) for x in range(10)]
#the range is 1,7 because 1 is inclusive, while 7 is exclusive. If it was 1,6, then it'll only count up to 5 not 6.
print(dice)

"""
Task 2 (random module):
Write a program that generates 5 random floating-point numbers between 0 and 1.
Then generate 5 random floating-point numbers between 10 and 20.
Print both sets of numbers.
"""
print("---Task 2---")

flts = [random.uniform(0.0, 1.0) for x in range(5)]
#The .uniform code works with the random module by generating random float withing the given range. randrange and randint only works with integers.
print(flts)
#The brackets in this code means that I am creating a list of 5 floating numbers, between the given numbers.
flts2 = [random.uniform(10.0, 20.0) for x in range(5)]
print(flts2)

"""
Task 3 (random module):
Create a list of colors: ["red", "blue", "green", "yellow", "purple"].
Write a program that randomly selects and prints 3 colors from this list without replacement.
"""
print("---Task 3---")

listy = ["red", "blue", "green", "yellow", "purple"]
colours = random.sample(listy, 3)
# The random.sample is basically used to select said items from the list, listy without replacement. Which means that once it's chosen, it won't be picked again.
#the 3 tells the code to select 3 different colours.
print(colours)

"""
Task 4 (random module):
Write a program that creates a list of numbers from 1 to 10, then shuffles the list
and prints the shuffled result.
"""
print("---Task 4---")

nums = [1,2,3,4,5,6,7,8,9,10]
#a list was created for the numbers.
random.shuffle(nums)
#the .shuffle code shuffles the numbers in the list into different order.
print(nums)