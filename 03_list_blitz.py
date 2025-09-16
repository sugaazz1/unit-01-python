"""
Task 1: Create a list
Create a list with 4 elements and print it.
"""
print("---Task 1---")

best_foods = ["Jollof rice", "Fried Rice", "Rice and Stew", "Meat Pie"]
#First step was to create a variable to store the list, which I named best_foods.
print(best_foods)
#printed it to see if it worked, and it did.
"""
Task 2: Add Element to a List
Add an element to the end of the list. Print the updated 
list.
"""
print("---Task 2---")

best_foods.append("Akara")
#To add to the list, we use code append which adds the element to the end of the list.
print(best_foods)
#i printed it to see if it was added and it was successful.
"""
Task 3: Remove Element from a List
Remove a specific element from the list. Print the 
updated list.
"""
print("---Task 3---")

best_foods.remove("Jollof rice")
#To remove a specific element from the list without going back, you can use the code .remove() to take an element away from the list.
print(best_foods)
#i printed it to see if it was deleted, and it was successful.
"""
Task 4: Modify Element in a List
Modify an element at a specific index with a new value. 
Print the updated list.
"""
print("---Task 4---")


best_foods[2] = "Fufu"
#To specically modify an element in the list, you put the list number, counting from zero up and change it into what ever you want to change.
print(best_foods)
#I printed it to see if I modified it, and it was successful


"""
Task 5: Append Multiple Elements to a List
Append multiple elements to the end of the list. Print 
the updated list.
"""
print("---Task 5---")

best_foods.append("Egusi soup")
best_foods.append("Banga Soup")
best_foods.append("Puff Puff")
#to add multiple elements to a list, you have to created a new best_foods.append() everytime, as you cannot put all together in one code.
print(best_foods)
#I printed it to see if it worked, and it did.

"""
Task 6: Delete Element at a Specific Index
Delete an element at a specific index. Print the updated 
list.
"""
print("---Task 6---")

del best_foods[3]
#To delete a specific element in the index, you say the number correspoding on the list counting from zero.
print(best_foods)
#I printed it to see if it was deleted and it was successful.

"""
Task 7: Slicing lists
Create a new variable equal to the first 2 items of your list
Then print out the new variable
"""
print("---Task 7---")

best_foods2 = ["Fried Rice", "Rice and Stew"]
#Created a new variable to store a portion of the first list.
print(best_foods2)
#i printed it and it worked.
"""
Task 8: Extend a List
Extend the list with the elements of another list. Print 
the updated list.
"""
print("---Task 8---")
best_foods_fr = best_foods + best_foods2

print(best_foods_fr)
#lastly, I created a new variable to add best_foods and best_foods2 to see if anything came out, and it did.