"""temperature = 75

if temperature > 80:
    print("It's hot")
elif temperature > 50:
    print("It's temperate")
else:
    print("It's cold")

    """

"""text = input("Hello, world, my name is ")
count = 0

for char in text:
    if char == " ":
       count += 1

print(count)
"""

print("give me a number")
n = int(input())

for num in range(1, n):
    if num % 2 == 0:
        print(num, "is even.")
    else:
        print(num, "is odd.")


num = int(input("Enter an integer: "))

if num < -1:
  print("No negative numbers.")
else:
  result = 1
  for i in range(1, num):
    result *= i
       

  print("Factorial of " + num + "is" + result)
