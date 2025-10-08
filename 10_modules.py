import os
import sys

"""
Task 1 (os module):
Write a Python program that prints the current folder (working directory) using the os module.
"""
something_som = os.getcwd()
print(something_som)
"""
Task 2 (os module):
Create a new directory called "test_folder" in the current directory.
Then print a list of all files and directories in the current directory.
"""
#test_folder = "hehe hope it works"
#os.mkdir(test_folder)
#print("Folders in directories", os.listdir(something_som))

#os.mkdir("test_folder")
#folder = os.listdir()

#print(folder)

"""
Task 3 (os module):
Write a program that checks if a directory called "data" exists in the current 
working directory. If it doesn't exist, create it. If it does exist, print 
"Directory already exists."
"""
if os.path.isdir("data") == True:
    print("Directory exists")
else: 
    print("Directory does not exists.")
    creat = input("create directory? ")
    if creat == "yes":
        os.mkdir("data")
        print("Directory created")


"""
Task 4 (os.path module):
Write a program that checks if a file called "config.txt" exists in the current directory.
If it exists, print its path. If it doesn't exist, print "File not found."
"""
os.getcwd()
print(os.getcwd())
os.listdir()
if not os.path.exists("config.txt"):
    print("File not found")
else:
    print("File found.")

"""
Task 5 (sys module):
Write a program that prints the Python version you are currently using.
"""
print(sys.version)

"""
Task 6 (sys module):
Write a program that prints the platform your Python interpreter is running on
(e.g., 'linux', 'win32', 'darwin'). The output should be user friendly names
"Linux", "Windows", "MacOS"
"""

if sys.platform.lower() == "darwin":
    print("macOS")