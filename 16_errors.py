"""
Identify the potential errors in the following code snippets and modify 
them to include appropriate try/except blocks to handle exceptions gracefully.
"""


"""
Example 1: Division
"""

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

def read_file(filename):
    try:
        file = open(filename, 'r')
        contents = file.read()
        print("File contents:", contents)
        file.close()
    except FileNotFoundError:
        with open("nonexistent.txt", "w") as file:
            filename = file.read()
# Example usage:
read_file("nonexistent.txt")

"""
Example 3: List Items
"""
"""
def get_item(lst, index):
    item = lst[index]
    print("Item:", item)

# Example usage:
my_list = [1, 2, 3]
get_item(my_list, 5)
"""

"""
Example 4: Dictionaries
"""
"""
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