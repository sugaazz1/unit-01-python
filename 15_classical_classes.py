"""
Task 1: People Class
Define a class called Person with attributes name and age.
Then, write a method within the class to introduce the person with their name and age.

Create a new object using this new class, and call the method you created.
"""
print("---Task 1---")
#This creates the class called Person
class Person:
    def __init__(self, name, age):
        self.name = name
#The attributes allows me to change and edit the names when needed.
        self.age = age

    def howdy(self):
        print("Howdy my name is " + self.name + ", and I am " +  str(self.age) + " years old")
#This method prints the greeting using the person's name and age.
Jordan = Person("Jordan", 152)
Jordan.howdy()


"""
Task 2: Animals Speak
Create a base class Animal with a empty method called speak. 

Then create two subclasses, Dog and Cat, each with their own speak method. 

Create objects using these subclasses and call the speak method.
"""
print("---Task 2---")
#created an animal class, by adding class before the name of your class.
class Animal:
    def speak(self):
        pass#The pass function makes the class empty as directed in the Task.
class Dog(Animal):#By putting the animal in the parenthesis next to dog, it becomes a sub class.
    def speak(self):
        print('Bark Bark')
class Cat(Animal):#Same case for cat. By putting the Animal inside the parathesis it also becomes a sub class.
    def speak(self):
        print('Meow Meow')

#created the 2 objects of cats and dogs, bypasses the 'pass' funciton under speak.
#And prints out the statement under the subclasses. So 'Meow' and 'Bark'.
meow = Cat().speak()
bark = Dog().speak()


"""
Task 3: Banking
Create a class BankAccount with attributes balance and owner. 

Include methods for depositing and withdrawing money, which should modify the balance attribute.

Test these methods with instances of the class.
"""
print("---Task 3---")

class BankAccount:
    def __init__(self, balance, owner):
        self.balance = balance
        self.owner = owner
    def deposit(self, cash):
        self.balance += cash
        print("")
    def withdraw(self, cash):
        self.withdraw -= cash
        print(f"You have withdrawed {self.withdraw}")
AccInfo = BankAccount(10000, "Billy")

AccInfo.deposit()
AccInfo.withdraw()

