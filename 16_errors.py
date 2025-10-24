"""
Identify the potential errors in the following code snippets and modify 
them to include appropriate try/except blocks to handle exceptions gracefully.
"""


"""
Example 1: Division
"""
print("---Example 1---")

def divide_numbers(num1, num2):
    try:
        result = num1 / num2
        print("Result:", result)
    except ZeroDivisionError: 
        print('You cannot divide by zero')
    except ValueError:
        print("You can't divide by strings/letters.")

divide_numbers(10, 3)
        


"""
Example 2: Opening Files 
""" 
print()

print("---Example 2---")
def read_file(filename):
    try:
        file = open(filename, 'r')
        contents = file.read()#This sets of code opens the file in read mode only.
        print("File contents:", contents)
        file.close()
    except FileNotFoundError:
 #If the code doesn't exist, this code handles it can creates a file instead of stopping the code.
        with open("nonexistent.txt", "w") as file:
            file.write("")#This creates an empty file. While the quotations is also a measure to confirm it exists.

read_file("nonexistent.txt")

"""
Example 3: List Items
"""

print("---Example 3---")

def get_item(lst, index):
    try:
        item = lst[index]
        print("Item:", item)
    except IndexError:
        

# Example usage:
my_list = [1, 2, 3]
get_item(my_list, 5)


"""
Example 4: Dictionaries
"""
"""
print("---Example 4---")

def get_value(dictionary, key):
    value = dictionary[key]
    print("Value:", value)

# Example usage:
my_dict = {"a": 1, "b": 2}
get_value(my_dict, "c")
"""

"""
Example 5: Else/Finally
Modify the following code to include an else block to execute code if no exceptions occur 
and a finally block to ensure that a certain action is always performed, regardless of whether an exception is raised.
"""

"""
print("---Example 5---")

def process_file(filename):
    try:
        with open(filename, 'r') as file:
            contents = file.read()
            print("File contents:", contents)
    except FileNotFoundError:
        print("Error: File not found.")

# Example usage:
process_file("example.txt")
"""