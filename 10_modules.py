import os
import sys

"""
Task 1 (os module):
Write a Python program that prints the current folder (working directory) using the os module.
"""
something_som = os.getcwd()
#To get the name of the current folder/directory  you are using, using an os module, you use os.getcwd()
print(something_som)
"""
Task 2 (os module):
Create a new directory called "test_folder" in the current directory.
Then print a list of all files and directories in the current directory.
"""
test_folder = "hehe hope it works"
#This is the variable that holds the name of the folder.
os.mkdir(test_folder)
#The os.mkdir() is a python code used to create folders/ directories. And it's going to print what the variable is equals to.
print("Folders in directories", os.listdir(something_som))



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
#I used conditional statement to check if a folder called data already existes. If so print that it exists.
else: 
    print("Directory does not exists.")
    creat = input("create directory? ")
    if creat == "yes":
        os.mkdir("data")
        print("Directory created")
#if the folder doesn't exist, it tells the user. Then it asks the user if they want to create the directory.

"""
Task 4 (os.path module):
Write a program that checks if a file called "config.txt" exists in the current directory.
If it exists, print its path. If it doesn't exist, print "File not found."
"""
os.getcwd()
print(os.getcwd())
os.listdir()
if not os.path.exists("config.txt"):#i used the .exists with path to check if it exists or not.
    print("File not found")
#This code basically just checks if a certain file is in the directory, if it is, it'll say found, if not, it'll say not found.
else:
    print("File found.")

"""
Task 5 (sys module):
Write a program that prints the Python version you are currently using.
"""
print(sys.version)
#The sys.version is the code that tells you what version of python you are currently using. sys = system
"""
Task 6 (sys module):
Write a program that prints the platform your Python interpreter is running on
(e.g., 'linux', 'win32', 'darwin'). The output should be user friendly names
"Linux", "Windows", "MacOS"
"""
#sys.platform tells the reader what operating system interpreter is running on. 
if sys.platform.lower() == "darwin":
    print("macOS")
elif sys.platform.lower() == "win32":
    print("Windows")
elif sys.platform.lower() == "linux":
    print("Linux")
#These other sys.platform checks if python is running on other different operating systems.