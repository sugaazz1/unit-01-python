"""text = input("Hello, world, my name is ")
count = 0

for char in text:
    if char == " ":
       count += 1

print(count)
"""

"""print("give me a number")
n = int(input())

for num in range(1, n):
    if num % 2 == 0:
        print(num, "is even.")
    else:
        print(num, "is odd.")
"""

"""num = int(input("Enter an integer: "))

if num < -1:
  print("No negative numbers.")
else:
  result = 1
  for i in range(-1, num):
    result *= num

  print("Factorial of " + num + "is" + result)
  """

"""attempts = 0
correct_password = "secret" 


while True:
    password = input("Enter your password: ")
    #attempts += 1
    if password.lower() == "incorrect_password":
        print("Correct password!")
        break
    else:
        attempts += 1
        print("Incorrect password")
        if attempts == 3:
            print("Too many attempts")
            break
"""
