"""
Exercise 1:
Write a program to print numbers from 1 to 10 using a for loop.
"""
print("---Task 1---")

for x in range(1,11):
    print(x)
#To print the numbers from 1-10, the first number "1" is inclusive, but the last number 11 is exclusive, that means the code will only count up to 10.

"""
Exercise 2:
Write a program to count by 10s from 900 to 1000
"""
print("---Task 2---")

for x in range(900, 1010, 10):
    print(x)
#Since the second number is always exclusive, the code stops before the specified number. A third number, means the number will count by 10.

"""
Exercise 3:
Write a program that counts form 1-100 by 9
"""
print("---Task 3---")

for x in range(1,109,9):
    print(x)
#Since we're trying to count to 100, from 1, we'll go up to 109, since we are counting by 9. And since the last number is exclusive "109" it'll stop the number before 109 which is 100

"""
Exercise 4:
Write a program to calculate the sum of all numbers from 1 to 10 using a for loop.
"""
print("---Task 4---")

hehehe = [1,2,3,4,5,6,7,8,9,10]
total = 0
#I created the variable to hold the number of list.
for x in hehehe:
    total += x
#the += adds the previous value to it self. So in this case, total = total+x.
    print(total)

"""
Excercise 5:
Uncomment the following code and run it. Then answer the following:
- What is the ouput of the code?
print("The output of this code is asteriks in ascending order.)

- Explain the iterative process that this code executes to get that output
#The rows = 5 variable is basically the break point for the "for" loop. Basically saying that Once there's a row of 5 asteriks, or just 5 rows, it'll stop the loop.
# While this snipet of code "for j in range(i + 1):" Apparently makes the code start from 1, then gradually, row by row add 1 until you get a row with 7 asteriks.

"""
print("---Task 5---")
rows = 7

for i in range(rows):
     for j in range(i + 1):
         print('*', end=' ')
     print()#Actually this is the print that makes sure it prints out row by row. SO row 1= 1, row 2 =2, and so on and so forth. Without it everything prints on a single line.