import random

"""
Task 1 (random module):
Write a program that simulates rolling a six-sided die 10 times.
Print each roll result.
"""
dice = random.randrange(1,7)
print(dice)

"""
Task 2 (random module):
Write a program that generates 5 random floating-point numbers between 0 and 1.
Then generate 5 random floating-point numbers between 10 and 20.
Print both sets of numbers.
"""


"""
Task 3 (random module):
Create a list of colors: ["red", "blue", "green", "yellow", "purple"].
Write a program that randomly selects and prints 3 colors from this list without replacement.
"""
listy = ["red", "blue", "green", "yellow", "purple"]
colours = random.sample(listy, 3)
print(colours)

"""
Task 4 (random module):
Write a program that creates a list of numbers from 1 to 10, then shuffles the list
and prints the shuffled result.
"""
nums = [1,2,3,4,5,6,7,8,9,10]
random.shuffle(nums)
print(nums)