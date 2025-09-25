"""
Exercise 1:
Write a program to print each character of a given string using a for loop.
"""
print("---Task 1---")

hehe = "I just wanna eatttt"
for x in hehe:
    print(x)
#This little code prints out the string inside the varible inside hehe as single character in a line.

"""
Exercise 2:
Write a program to calculate the sum of elements in a list using a for loop.
"""
print("---Task 2---")

summy = [1,2,3,4,5,6,7,8,9,10]
total = 0
#I created the variable to hold the number of list.
for x in summy:
    total += x 
    print(total)
#the += adds the previous value to it self. So in this case, total = total+x.

"""
Exercise 3:
Write a program to print the length of each word in a sentence using a for loop and a list.
"""
print("---Task 3---")

listy = ["Turkey", "Beans", "Potato", "Yams", "Gravy", "YOU NAMEEE ITTT"]
#This list holds the various string.
for list in listy:
    print(len(list))
#The len() prints out the length of each letter as numbers. For example, turkey as 6 letters, so it prints out 6.
"""
Excercise 4:
Write a program that creates a dictionary (atleast 4 key:value pairs) and then
iterates through a dictionary and prints the result

In a comment, answer the following, what do you notice about the output of your code?
Is it what you expected?
"""
print("---Task 4---")

my_dict = {
    "Banana": 6,
    "Watermelon": 2,
    "Papaya": 4, 
    "Blueberries" : 50
}

for x in my_dict:
    print(x)
    print(my_dict[x])
#This little code "print(my_dict[x])" prints the number of each items that's in the dictionary out. 

#print(my_dict["Banana"])




