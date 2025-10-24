"""
Identify the potential errors in the following code snippets and modify 
them to include appropriate try/except blocks to handle exceptions gracefully.
"""


"""
Example 1: Division
"""
print("---Example 1---")

def divide_numbers(num1, num2):
    """#This defines a function that divides two numbers"""
    try:#The try is used to gracefully handle exceptions incase the user wants to do something stupid. Such as dividing by 0.
        result = num1 / num2
        print("Result:", result)
    except ZeroDivisionError: 
        print('You cannot divide by zero')#If the user puts in a zero, this message pops up, as you can't divide by 0.
    except ValueError:
        print("You can't divide by strings/letters.")#This message pops up if they put in anything other than numbers.

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
    except FileNotFoundError:#Used to handle the error in the instance that no such file exists.
        print("No such file exists.")#If the file doesn't exist, per the 'FileNotFoundError' this message will pop up.

read_file("nonexistent.txt")


"""
Example 3: List Items
"""
print()

print("---Example 3---")

def get_item(lst, index):
    try:
        item = lst[index]
        print("Item:", item)
    except IndexError:#if there's an index error, asking for a list that's not in your list, this code handles that error instead of crashing.
        print("Value not included in the list.")#This message prints out instead.

# Example usage:
my_list = [1, 2, 3]
get_item(my_list, 5)


"""
Example 4: Dictionaries
"""
print()

print("---Example 4---")

def get_value(dictionary, key):

    try:#This try block will check if the key the user is asking for is inside the dictionary.
        value = dictionary[key]
        print("Value:", value)
    except KeyError:#iF the key the user is asking for isn't inside the dictionary, this except will handle that error.
        print("No such value in the dictionary.")#This message will print if there is an error.
        
# Example usage:
my_dict = {"a": 1, "b": 2}
get_value(my_dict, "c")


"""
Example 5: Else/Finally
Modify the following code to include an else block to execute code if no exceptions occur 
and a finally block to ensure that a certain action is always performed, regardless of whether an exception is raised.
"""


print("---Example 5---")

def process_file(filename):
    """This function similar to example one, tries to open and read a file."""
    try:
        with open(filename, 'r') as file:
            contents = file.read()
            print("File contents:", contents)
    except FileNotFoundError:#If the file doesn't not exist, this except handles the error.
        print("Error: File not found.")#This message prints out instead of the code crashing.
    else:#If it does exist, this code runs. and the message prints.
        print("Opening File....")
    finally :#Lastly, this code runs no matter what. It's also a way for you to check if the code is running or not.
        print("The file you are looking for may or may not exist.")
# Example usage:
process_file("example.txt")
