# while True:
#     a, b, c = map(int, input("Enter three numbers separated by spaces: ").split())
#     
#     if a >= b and a >= c:
#         greater = a
#     elif b >= a and b >= c:
#         greater = b
#     else:
#         greater = c
#     
#     print("Greater Number: ", greater)

# while True:
#    a, b, c = map(int ,input("Enter three numbers: ").split());
#    
#    if a >= b and a >= c:
#        greater = a
#    elif b >= a and b >= c:
#        greater = b
#    else:
#     greater = c
#     
#     print("Greater Number: ",greater)

# n = input("Enter a bianry: ")
# b = int(n, 2)
# print("Value: ", b)
# rows = 3
# cols = 6
# for i in range(rows):
#     for j in range(cols):
#         if i == 0 or i == 2 or j == 0 or j == cols - 1:
#             print("0", end=" ")
#         else:
#             print(" ", end="")  # No extra spaces, just a single space in the middle
#     print()  # Move to the next row

# rows = 4
# for i in range(1, rows + 1):
#     # Print leading spaces
#     print("  " * (rows - i), end="  ")
# 
#     for j in range(1, i + 1):
#         if j == 1 or j == i:  # Print 'A' at the beginning or end of the row
#             print(" A ", end="  ")
#         else:  # Print spaces between 'A's
#             print("  " * (2 * (j - 1) - 1), end="  ")
# 
#     print()  # Move to the next line


# rows = 4  # Number of rows
# 
# for i in range(1, rows + 1):
#     # Calculate the spaces before the first "A"
#     print(" " * (rows - i), end="")  
#     
#     # Print the first "A"
#     print("A", end="")
#     
#     # Add spaces between "A"s for the current row
#     if i > 1:
#         print(" " * (2 * (i - 1) - 1), end="")
#         print("A", end="")  # Print the second "A"
#     
#     print()  # Move to the next row
# Number of rows for the pattern
# rows = 6
# columns = 6
# 
# # Number of rows for the pattern
# rows = 6
# columns = 6
# 
# for i in range(1, rows + 1):
#     if i == 1 or i == rows:
#         # Print 'o' for the top and bottom rows
#         print("o  " * columns)
#     else:
#         # Print 'o' at the start and end with equal spacing in between
#         print("o" + " " * (3 * (columns - 2) - 1) + "o")

# rows = 6  # Number of rows
# 
# for i in range(rows):
#     print("  " * i + "  * " * (rows - i))
# 
# import math
# 
# num = int(input("Enter a number: "))
# if num < 0:
#     print("Factorial is not defined for negative numbers.")
# else:
#     print("Factorial of", num, "is", math.factorial(num))
# Take user input for the number
# num = int(input("Enter a number: "))
# 
# # Take user input for the range of the table
# table_range = int(input("Enter the range for multiplication table: "))

# Display multiplication table
# print(f"\nMultiplication Table of {num} up to {table_range}:")
# for i in range(1, table_range + 1):
#     print(f"{num} x {i} = {num * i}")

# def add(x, y):
#     return x + y
# 
# def subtract(x, y):
#     return x - y
# 
# def multiply(x, y):
#     return x * y
# 
# def divide(x, y):
#     if y == 0:
#         return "Error! Division by zero."
#     return x / y
# 
# while True:
#     # Get user choice for operation
#     choice = input("Enter choice (+, -, *, /): ")


    # Ensure the user enters valid numbers
#     if choice in ('+', '-', '*', '/'):
#         try:
#             num1 = float(input("Enter first number: "))
#             num2 = float(input("Enter second number: "))
# 
#             if choice == '+':
#                 print(f"Result: {num1} + {num2} = {add(num1, num2)}")
#             elif choice == '-':
#                 print(f"Result: {num1} - {num2} = {subtract(num1, num2)}")
#             elif choice == '*':
#                 print(f"Result: {num1} * {num2} = {multiply(num1, num2)}")
#             elif choice == '/':
#                 print(f"Result: {num1} / {num2} = {divide(num1, num2)}")
#         except ValueError:
#             print("Invalid input! Please enter valid numbers.")
#     else:
#         print("Invalid choice! Please enter a valid operation (+, -, *, /).")

# def compute_hcf(x, y):
#     while y:
#         x, y = y, x % y
#     return x
# 
# def compute_lcm(x, y):
#     return (x * y) // compute_hcf(x, y)
# 
# # Taking input from user
# num1 = int(input("Enter first number: "))
# num2 = int(input("Enter second number: "))
# 
# hcf = compute_hcf(num1, num2)
# lcm = compute_lcm(num1, num2)
# 
# print(f"HCF of {num1} and {num2} is {hcf}.")
# print(f"LCM of {num1} and {num2} is {lcm}.")
# def is_prime(n):
#     if n < 2:
#         return False  # Numbers less than 2 are not prime
#     for i in range(2, int(n ** 0.5) + 1):  # Check divisibility up to √n
#         if n % i == 0:
#             return False
#     return True
# 
# # Input from user
# num = int(input("Enter a number: "))
# 
# # Check and display result
# if is_prime(num):
#     print(f"{num} is a Prime number.")
# else:
#     print(f"{num} is not a Prime number.")
# num = int(input("Enter a number: "))
# 
# if num < 2:
#     print(f"{num} is not a Prime number.")
# else:
#     is_prime = True
#     for i in range(2, int(num ** 0.5) + 1):  # Checking divisibility up to √num
#         if num % i == 0:
#             is_prime = False
#             break  # Exit loop early if a divisor is found
# 
#     if is_prime:
#         print(f"{num} is a Prime number.")
#     else:
#         print(f"{num} is not a Prime number.")


# year = int(input("Enter a year: "))
# 
# # A year is a leap year if:
# # 1. It is divisible by 4 AND (not divisible by 100 OR divisible by 400)
# if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
#     print(f"{year} is a Leap Year.")
# else:
#     print(f"{year} is not a Leap Year.")

# 
# # Define the matrices
# matrix1 = [[1, 2, 3], 
#            [4, 5, 6], 
#            [7, 8, 9]]
# 
# matrix2 = [[9, 8, 7], 
#            [6, 5, 4], 
#            [3, 2, 1]]
# 
# # Create an empty result matrix
# result = [[0, 0, 0], 
#           [0, 0, 0], 
#           [0, 0, 0]]
# 
# # Adding two matrices
# for i in range(len(matrix1)):      # Loop through rows
#     for j in range(len(matrix1[0])):  # Loop through columns
#         result[i][j] = matrix1[i][j] + matrix2[i][j]
# 
# # Print the result
# print("Sum of matrices:")
# for row in result:
#     print(row)
#     
#     
#     
# # Get matrix size from user
# rows = int(input("Enter number of rows: "))
# cols = int(input("Enter number of columns: "))
# 
# # Function to take matrix input
# def input_matrix(name):
#     print(f"Enter elements of {name} matrix row-wise:")
#     matrix = []
#     for i in range(rows):
#         row = list(map(int, input().split()))  # Take space-separated input
#         matrix.append(row)
#     return matrix
# 
# # Input two matrices
# matrix1 = input_matrix("First")
# matrix2 = input_matrix("Second")
# 
# # Initialize result matrix
# result = [[0 for _ in range(cols)] for _ in range(rows)]
# 
# # Adding two matrices
# for i in range(rows):
#     for j in range(cols):
#         result[i][j] = matrix1[i][j] + matrix2[i][j]
# 
# # Print the result matrix
# print("Sum of the matrices:")
# for row in result:
#     print(row)

# print('I read in "ICFAI UNIVERSITY".')
# OR
# print("I read in \"ICFAI UNIVERSITY\".")

# n = input("Enter a number: ")
# 
# digit = len(n)
# 
# print("Number of digits: ", digit)

# n = int(input("Enter a number: "))
# binary = bin(n)
# print(f"Binary number of {n}: ",binary)

# n = int(input("Enter a number: "))
# if n % 2 == 0:
#     print(f"The number {n} is even.")
# else:
#     print(f"The number {n} is odd.")

# n = input("Enter a number: ")
# 
# n_digit = len(n)
# print(f"Number of digits in {n} is:",n_digit)

# while True:
#   n,m,p = map(int,input("\nEnter three number with spacing: ").split())
#   if n>m and n>p:
#     print(f"{n} is the greater number.")
#   elif m>n and m>p:
#         print(f"{m} is the greater number.")
#   elif n==m==p:
#             print("All numbers are equal.")
#   else:
#             print(f"{p} is the greater number.")

# import math
# 
# n = int(input("Enter a number: "))
# if n<0:
#     print("Factorial of negetive number is not defined.")
# else:
#         print(f"The factorial of {n} is: ",math.factorial(n))

# import math
# 
# n = int(input("Enter a number: "))
# 
# print(f"The square root of {n} is: ",math.sqrt(n))

# import math
# n = int(input("Enter a number: "))
# p = int(input(f"Enter the power of {n}: "))
# power = math.pow(n, p)
# print(f"The result is: ",power)

# n = int(input("Enter a number: "))
# if n<0:
#     print(f"{n} is a negative number.")
# if n==0:
#     print(f"{n} is neither positive nor negative.")
# else:
#         print(f"{n} is a positive number.")

# import numpy as np
# 
# a = np.array([[1, 2, 3], [4, 5, 6], [7, 5, 8]])
# b = np.array([[1, 2, 3], [4, 5, 6], [7, 5, 8]])
# 
# result = np.dot(a, b)
# 
# print("The matrix multiplication is: ")
# for row in result:
#     print(row)

# import numpy as np
# 
# A = np.array([[1, 2], [3, 4]])
# Bxc = np.array([[1, 2], [3, 4]])
# 
# result = np.dot(A, B)
# 
# print("Multiplication of 2x2 matrix: ")
# for row in result:
#     print(row)


# n = input("Enter a binary number: ")
# dn = int(n, 2)
# hexn = hex(dn)
# print(f"Hexadecimal representation of binary {n} is: {hexn}")

# import numpy as np
# 
# a = np.array([[1, 2, 4], [5, 6, 10], [10, 5, 4]])
# b = np.array([[1, 2, 4], [5, 6, 10], [10, 5, 4]])
# 
# result = np.dot(a, b)
# 
# print("Matrix mul of 2x2: ")
# for row in result:
#  cprint(row)
 
# n = int(input("Enter a number: "))
# if n<2:
#     print(f"{n} is not a prime number.")
# else:
#     prime = True
#     for i in range(2,int(n ** 0.5)+1):
#         if n % i == 0:
#             prime = False
#             break
# if prime:
#     print(f"{n} is a Prime number.")
# else:
#     print(f"{n} is not a Prime number.")


# while True:
# 
#  y = int(input("\nEnter a year: "))
#  if (y%4==0 and y%100!=0 or y%400==0):
#     print(f"{y} is a Leap Year.")
# else:
#     print(f"{y} is not a Leap Year.")

# n = int(input("Enter a number: "))
# if n%2==0:
#     print(f"{n} is a even number.")
# else:
#     print(f"{n} is a odd number.")

# import math
# n = int(input("Enter a number: "))
# m = int(input(f"Enter the power of {n}: "))
# print(f"Result:", pow(n, m))


# n = int(input("Enter the number want to print all even no.: "))
# print(f"Even numbers upto {n} is:")
# for i in range(1, n+1):
#     if i%2!=0:
#         print(i)

# n = int(input("Enter a number: "))
# if n>1:
#     composite = False
#     for i in range(2, n):
#         if n % i ==0:
#             composite = True
#             break
#         
# if composite:
#     print(f"{n} is a Composite Number.")
# else:
#         print(f"{n} is not a Composite")
        
# for i in range(1, 5+1):
#    print(i)

# print("A simple Calculator")
# while True:
#     
#  operator = input("\nEnter Operator(+,-,*,/): ")
#  n = float(input("\nEnter First number: "))
#  m = float(input("Enter Second number: "))
#   
#  if operator == "+":
#       print(f"{n} + {m} = ",n+m)
#  elif operator == "-":
#       print(f"{n} - {m} = ",n-m)
#  elif operator == "*":
#       print(f"{n} * {m} = ",n*m)
#  elif operator == "/":
#      if m and n!=0:
#          print(f"{n} / {m} = ",n/m)
#      else:
#          print("Error! Divided by zero is not possible.")


# matrix = ([[1, 2], [3, 4]])
# 
# scalar = int(input("Enter the scalar value: "))
# 
# result = [[scalar * element for element in row] for row in matrix]
# 
# print("Resultant matrix after scalar multiplication:")
# for row in result:
#     print(row)
# 
#      
 

# a = int(input("A: "))
# b = int(input("B: "))
# n = a
# a = b
# b = n
# print("After swaping: ")
# print("A:",a)
# print("B:",b)
#  

# def greet():
#     print("Hellow")
#     greet()

# n = float(input("Enter temperature in celsius: "))
# print(f"Fehrenhite of {n}°C is: ",(n*9/5)+32,"°F")

# n = int(input("Enter any number: "))
# if n<2:
#     print(f"{n} is not a Prime number.")
# else:
#     prime = True
#     for i in range(2, int(n**0.5)+1):
# if n % i == 0:
#     prime = False
#     break
#     
# if prime:
#     print(f"{n} is a Prime number.")
# else:
#     print(f"{n} is not a Prime number.")

# n, m = map, float(input("Enter a no.: ").split())
# print(n+m)

# import random
# r_n = random.randint(2, 3)
# if r_n == 3:
#     print("You are pookie.")
# else:
#     print(f"{r_n}")

# n = (int(input("Enter a number upto want: ")))
# for i in range (1, n+1):
#  print(i)
#  
# m = (int(input(f"Enter a numbers you want to select from 1 to {n}: ")))

# arr = list(map(int, input("Enter numbers separated by space: ").split()))
# print(arr)
# missing_values = set(range(1, max(arr) + 1)) - set(arr)
# print("Missing values:", sorted(missing_values))

# import numpy as np
# a = np.array([[1, 2],[2,4]])
# b = np.array([[5, 4], [1, 4]])
# result = np.dot(a ,b)
# print("The Multiplication of 2X2 matrix: ")
# for row in result:
#     print(row)

# import random
# r_n = random.randint(1, 100)
# print("Random number is: ",r_n)

# import random
# print("The random number is: ",random.randrange(10+1))

# import random
# random_n = random.randrange(10+1)
# print(f"{random_n} is the Random number.")

# n = int(input("Enter the Mile: "))
# kilometre = n/0.621371
# print(f"{n} Mile = {kilometre} KM")

# n = int(input("Enter the Celcius: "))
# fah = (n*9/5)+32
# print(f"{n} C = {fah} F.")

# text = input("Enter the string or words: ")
# vowels = "aeiouAEIOU"
# count = sum(1 for char in text if char in vowels)
# print("Number of vowels:", count)

# # Read from input file
# with open("input.txt", "r") as infile:
#     lines = infile.readlines()
#     word_line = lines[0].strip()  # Line with words
#     string_line = lines[1].strip()  # Line for vowel count
# 
# # Part 1: Sort words
# words = word_line.split()
# words.sort()
# 
# # Part 2: Count vowels
# vowels = "aeiouAEIOU"
# vowel_count = sum(1 for char in string_line if char in vowels)
# 
# # Write to output file
# with open("output.txt", "w") as outfile:
#     outfile.write("Sorted Words: " + " ".join(words) + "\n")
#     outfile.write("Number of Vowels: " + str(vowel_count) + "\n")
# 

# words = ["banana", "apple", "grape", "cherry", "date"]
# words.sort()
# print("Sorted words:", words)

# a, b, c = map(int, input("Enter three numbers separated by spaces: ").split())
# 
# if a >= b and a >= c:
#     greater = a
# elif b >= a and b >= c:
#     greater = b
# else:
#     greater = c
# 
# print(f"{greater} is the greatest number.")
# n, m = map(int, input("Enter two numbers separated by space: ").split())
# print(f"{n} + {m} = {n+m}")
# while True:
#  import math
#  n = float(input("Enter a number: "))
#  if n>0:
#     sqr = math.sqrt(n)
#     print(f"The square root is: {sqr}")
#  else:
#         print("Square root of negative numebr is not real.")

# a = int(input("A: "))
# b = int(input("B: "))
# n = a
# a = b
# b = n
# print(f"A: ",a)
# print(f"B: ",b)
# n = int(input("Enter a number: "))
# if n%2==0:
#     print(f"{n} is a Even number.")
# else:
#     print(f"{n} is a Odd number.")
# while True:
#  n = int(input("Enter a number: "))
#  print(f"The binary number of {n} is: ",hex(n))

# n = input("Enter the decimal: ")
# print(f"The decimal number of {n} is: ",int(n, 16))
 
# n = int(input("Enter a number: "))
# 
# if n <= 1:
#     print(f"{n} is not a prime number.")
# else:
#     prime = True
#     for i in range(2, int(n**0.5) + 1):
#         if n % i == 0:
#             prime = False
#             break
# 
#     if prime:
#         print(f"{n} is a prime number.")
#     else:
#         print(f"{n} is not a prime number.")

# year = int(input("Enert a year: "))
# if year%4==0 and year%100!=0 or year%400==0:
#     print(f"{year} is Leap Year.")
# else:
#     print(f"{year} is not a Leap Year.")

# import numpy as np
# a = np.array([[2, 3], [5, 6]])
# b = np.array([[2, 3], [5, 6]])
# result = np.dot(a, b)
# print("The matrix mul of 2X2: ")
# for row in result:
#     print(row)

# import random
# r_n = random.randrange(1, 100)
# print(f"Random number: ",r_n)

# n = int(input("Enter the Miles: "))
# km = n/0.621371
# print(f"{n} Mile = {km} Km.")

# c = int(input("Enter the Celcius: "))
# fah = (c*9/5)+32
# print(f"{c} Celcius = {fah}F.")
# import time
# numbers = list(map(int, input("Enter list elements separated by space: ").split()))
# print("Your List is:", numbers)
# 
# start_time = time.time()
# element = int(input("Enter the element you want to search: "))
# if element in numbers:
#     index = numbers.index(element)
#     print(f"Found in index {index}")
# else:
#     print(f"Not found in the list.")
#     
#     
# end_time = time.time()
# runtime = end_time - start_time
# print(f"Runtime of this code: {runtime} seconds")

# import time
# start_time = time.time()
# n = int(input("Enter a number: "))
# 
# if n<=1:
#     print(f"{n} is Not a Prime number.")
# else:
#     for i in range(2, n):
#         if n%i == 0:
#             print(f"{n} is Not a Prime number.")
#             break
#     else:
#             print(f"{n} is a Prime number.")
#             
# end_time = time.time()
# runtime = end_time - start_time
# print(f"Runtime of this code: {runtime} seconds"
# n = int(input("Enter a number: "))
# def countdown():
#     if n == 0:
#         print("Done!")
#     else:
#         print(n)
#         countdown(n - 1)  # the function calls itself

# words = input("Enter some words: ").split()
# words.sort()
# print("Sorted words: ",words)

# text = input("Enter a string: ")
# vowels = "aeiouAEIOU"
# count = sum(1 for char in text if char in vowels)
# print(count)
# Read two numbers from input.txt
# with open("input.txt", "r") as file:
#     lines = file.readlines()
#     a = int(lines[0])
#     b = int(lines[1])
# 
# # Add the numbers
# result = a + b
# 
# # Write the result to output.txt
# with open("output.txt", "w") as file:
#     file.write(f"The sum of {a} and {b} is {result}")
# 
# print("Result written to output.txt")
# n = int(input("Enter a number: "))
# if n<1:
#     print(f"{n} is not a Prime number.")
# else:
#     for i in range(2, int(n**0.5)+1):
#         if n%i == 0:
#             print(f"{n} is not a Prime number.")
#             break
#     else:
#         print(f"{n} is a Prime number.")
# n = int(input("Enter a number: "))
# if n%2==0:
#     print(f"{n} is even number.")
# else:
#      print(f"{n} is odd number.")
# n = int(input("Enter a year: "))
# if n%4==0 and n%100!=0 or n%400==0:
#     print(f"{n} is a Leap year.")
# else:
#     print(f"{n} is not a Leap year.")
# import numpy as np
# # a = np.array([[1, 4, 7], [2, 5, 8], [3, 6, 9]])
# a = np.array([[8, 2], [4, 3]])
# result = np.linalg.det(a)
# print(f"Matrix Determinant is: ",result)
# a, b, c = map(int, input("Enyer three numbers after spacing: ").split())
# if a==b==c:
#     print("All numbers are same.")
# elif a>=b and a>=c:
#     print(f"{a} is greator among three.")
# elif b>=a and b>=c:
#     print(f"{b} is greator among three.")
# else:
#     print(f"{c} is greator among three.")

# print("It is a Simple Calculator...")
# choice = input("Enter the operator (+,-,/,*): ")
# a, b = map(float, input(f"Enter two numbers separated by spacing: ").split())
# if choice == '+':
#     print(f"{a} + {b} = {a+b}")
# elif choice == '-':
#     print(f"{a} - {b} = {a-b}")
# elif choice == '*':
#     print(f"{a} * {b} = {a*b}")
# elif choice == '/':
#     if b == 0:
#         print("Error!! Can't divided by zero.")
#     else:
#         print(f"{a} / {b} = {a/b}")
# else:
#     print(f"{choice} is a Invalid Operator.")

# print("This is s Percentage calculator (%)...")
# a = float(input("Enter how much you got: "))
# b = float(input("Enter the total marks out of this: "))
# print(f"Your percentage of {a} outoff {b} is: {a/b*100}%")

# n = 86785
# num = n
# count = 0
# while num>0:
#     count+=1
#     num=num//10
# print(f"{n} has {count} digits.")

# n = 10
# while n>0:
#     r_d = n%10
#     print(r_d, end="")
#     n=n//10
# from math import*
# def countDigits(n):
#     return len(str(n))
# 
# print(countDigits(9884))

# from math import*
# def countDigits(n):
#     if n == 0:
#         return 1
#     return floor(log10(n))+1
# 
# print(countDigits(786785))
# import random
# print(random.randint(1, 2))

# n = int(input("Enter a number to check: "))
# o = n
# r_d = 0
# while o>0:
#     digit = o%10
#     r_d = r_d*10+digit
#     o=o//10
# if n == r_d:
#     print("Palindrome.")
# else:
#     print("Not palindrome.")

# n = int(input("Enter a number to find factors: "))
# result = []
# if n == 0:
#     print("0 has infinitely many factors.")
# else:
#     for i in range (1, n+1):
#         if n % i == 0:
#             result.append(i)
#         
#     print(result)
# n = 10
# result = []
# for i in range (1, n//2+1):
#     if n%i == 0:
#         result.append(i)
# result.append(n)
# print(result)
# from math import sqrt
# n = 10
# result = []
# for i in range (1, int(sqrt(n))+1):
#     if n % i == 0:
#         result.append(i)
#         if n//i!=i:
#             result.append(n//i)
# result.sort()
# print(result)          

# n = 184481
# num = n
# res = 0
# while n>0:
#     digit = n % 10
#     res = res*10 + digit
#     n=n//10
# if num == res:
#     print("Palindrome.")
#     
# else:
#     print("Not palondrome.")

# n = 12
# count = 0
# result = []
# for i in range(1, n+1):
#     if n%i == 0:
#         result.append(i)
# print(result)
#         
# nums = [1, 2, 3, 1, 5]
# freq_main = dict()
# 
# for i in range(len(nums)):
#     if nums[i] in freq_main:
#         freq_main[nums[i]] += 1  # increment existing count
#     else:
#         freq_main[nums[i]] = 1   # initialize count to 1
# 
# print(freq_main)

# nums = [1, 2, 2, 3, 2, 56, 2]
# hash_map = dict()
# n = len(nums)
# for i in range(0, n):
#     hash_map[nums[i]] = hash_map.get(nums[i], 0)+1
# print(hash_map)

# n = 12
# num = n
# res = []
# if n == 0:
#     print(f"{n} has infinite factors.")
# else:
#     for i in range (1, abs(n)+1):
#          if n % i == 0:
#              if n>0:
#                  res.append(i)
#              else:
#                  res.append(-i)
#     res.sort()
#     print(res)

# n = [1, 2, 2, 3, 2, 56, 2]
# m = [1, 2, 3, 56]
# hash_map = dict()
# for num in m:
#     count = 0
#     for x in n:
#         if x == num:
#             hash_map[num]= n.count(num)
# print(hash_map)


# s = "azyxyyzaaaa"
# q = ["d", "a", "y", "x"]
# 
# hash_list = [0] * 26
# for ch in s:
#     ascii_val = ord(ch)
#     index = ascii_val - 97
#     hash_list[index] += 1
#     
# for char in q:
#     index = ord(char) - 97
#     print(char,":",hash_list[index])

# def sum(a, b):
#     return a + b
# print(sum(1,2))
    
# s = "azyxyyzaaaa"
# q = ["d", "a", "y", "x"]
# res = dict()
# for i in range(len(q)):
#     char = q[i]
#     res[char] = s.count(char)
# print(res)

# a = [2, 1, 2, 1, 6, 6, 9]
# b = [1, 3, 6]
# res = dict()
# for i in range(len(b)):
#     n = b[i]
#     res[n] = a.count(n)
# print(res)

# a = [2, 1, 2, 1, 6, 6, 9]
# res = dict()
# for i in range(0, len(a)):
#     res[a[i]] = res.get(a[i], 0)+1
# print(res)

# s = [1, 2, 2]
# res = dict()
# for i in range(len(s)):
#     n = s[i]
#     res[n] = s.count(n)
# print(res)

# num = 101
# n = 3
# for i in range(0, n):
#     print(f"{num}")

# def func(x, n):
#     if n == 0:
#         return
#     print(x)
#     func(x, n-1)
# func(3, 6)
# n = 6
# for i in range(1, n+1):
#     print(i)

# def func(i, n):
#     if i>n:
#         return
#     print(i)
#     func(i+1, n)
# func(1, 4)

# def func(n):
#     if 1>n:
#         return
#     func(n-1)
#     print(n)
# func(3)

# def func(x, n):
#     if n == 0:
#         return
#     print(x)
#     func(x, n-1)
# func(1, 4)

# def func(x, n):
#     if n == 0:
#         return
#     func(x, n-1)
#     print(x)
# func(1, 3)

# def funct(n):
#     for i in range(1, n+1):
#         print(i)
# funct(5)

# n = 2020
# num = n
# res = 0
# while n>0:
#     digit = n % 10
#     res = res*10+digit
#     n = n//10
# if num == res:
#     print("Palindrome.")
# else:
#     print("Not Palindrome.")

# year = 1900
# if year % 400 == 0:
#     print("Leap Year.")
# elif year % 100 == 0:
#     print("Not Leap Year.")
# elif year % 4 == 0:
#     print("Leap Year.")
# else:
#     print("Not Leap Year.")

# n = 6
# count = 0
# if n == 0:
#     print("0 has infinitely many divisors.")
# elif n == 1:
#     print("1 is neither prime nor composite.")
# else:
#     for i in range(1, n+1):
#     if n % i == 0:
#         count+=1
# if count>=2:
#     print("Not a Prime Number.")
# else:
#     print("Prime Number.")
    
# n = 31
# count = 0    
# for i in range(1, n+1):
#     if n % i == 0:
#         count+=1
# if count>2:
#     print("Not a Prime Number.")
# else:
#     print("Prime Number.")

# n = "aabbccdca"
# s = ["a", "b", "c", "d"]
# res = {}
# for i in range(0, len(s)):
#     freq = s[i]
#     res[freq] = n.count(freq)
# print(res)

# s = "aababacccdc"
# n = len(s)
# longest = ""
# for i in range(n):
# #Odd length Palindrome
#     left = i
#     right = i
#     while left >= 0 and right < n and s[left] == s[right]:
#         if (right - left + 1) > len(longest):
#             longest = s[left:right + 1]
#         left -= 1
#         right += 1
# #Even Length palindrome
#     left = i
#     right = i + 1
#     while left >= 0 and right < n and s[left] == s[right]:
#         if (right - left + 1) > len(longest):
#             longest = s[left:right + 1]
#         left -= 1
#         right += 1
# print(longest)
# 
# def func(x, n):
#     if n == 0:
#         return
#     func(x, n-1)
#     print(n)
# func(1, 4)

# def prime(n):
#     count = 0
#     for i in range(1, n+1):
#         if n % i == 0:
#             count+=1
#     if count>2:
#         print("Not Prime.")
#     else:
#         print("Prime.")
# prime(11)

# s = "abacac"
# n = len(s)
# longest = ""
# for i in range(n):
#     l = i
#     r = i
#     while l >= 0 and r < n and s[l] == s[r]:
#         if (r - l + 1) > len(longest):
#             longest = s[l : r + 1]
#         l -= 1
#         r += 1
#     l = i
#     r = i + 1
#     while l >= 0 and r < n and s[l] == s[r]:
#         if (r - l + 1) > len(longest):
#             longest  = s[l : r + 1]
#         l -= 1
#         r += 1
# print(longest)
# n = 4
# sum = 0
# for i in range(1, n+1):
#     sum +=i
# print(sum)

# def func(n):
#     sum = 0
#     if n == 0:
#         return
#     for i in range(1, n+1):
#         sum += i
#     print(sum)
#     
# func(10)

# def func(sum, i, n):
#     if i>n:
#         print(sum)
#         return
#     func(sum+i, i+1, n)
# func(0, 1, 4)

# def func(n):
#     if n == 1:
#         return 1
#     return n+func(n-1)
# n = 4
# x = func(n)
# print(x)

# def func(mul, i, n):
#     if i>n:
#         print(mul)
#         return
#     func(mul*i, i+1, n)
# func(1, 1, 4)
# s = "aaba"
# n = len(s)
# longest = ""
# for i in range(n):
#     left = i
#     right = i
#     while left >= 0 and right < n and s[left] == s[right]:
#         if (right - left + 1) > len(longest):
#             longest = s[left : right + 1]
#         left -= 1
#         right += 1
#     left = i
#     right = i+1
#     while left >= 0 and right < n and s[left] == s[right]:
#         if (right - left + 1) > len(longest):
#             longest = s[left : right + 1]
#         left -= 1
#         right += 1
# print(longest)

# s = ["aabbaa"]
# n = "a", "b"
# res = dict()
# for i in range (len(n)):
#     char = n[i]
#     res[char] = s.count(char)
# print(res)

# s = [1, 2, 2, 1, 8]
# n = [1, 2, 3, 8]
# res = dict()
# for i in range(len(n)):
#     a = n[i]
#     res[a] = s.count(a)
# print(res)

# n = 12
# res = []
# for i in range(1, n//2+1):
#     if n % i == 0:
#         res.append(i)
# res.append(n)
# print(res)

# def func(n):
#     count = 0
#     for i in range(1, n+1):
#         count += i
#     print(count)
# func(4)
    
# s = "1162611"
# n = len(s)
# longest = ""
# for i in range(n):
#     left = i
#     right = i
#     while left >= 0 and right < n and s[left] == s[right]:
#         if (right - left + 1) >  len(longest):
#             longest = s[left: right + 1]
#         left -= 1
#         right += 1
#     left = i
#     right = i+1
#     while left >= 0 and right < n and s[left] == s[right]:
#         if (right - left + 1) >  len(longest):
#             longest = s[left: right + 1]
#         left -= 1
#         right += 1
# 
# print(longest)

# def func(sum, i, n):
#     if i>n:
#         print(sum)
#         return
#     func(sum+i, i+1, n)
# func(0, 1, 10)

# def func(x, n):
#     if n == 0:
#         return
#     print(x)
#     func(x, n-1)
# func(10, 4)

# import random
# otp = random.randint(100000, 999999)
# print("OTP:",otp)
# n = int(input("Enter OTP: "))
# if n == otp:
#     print("Verified Suceefully.")
# else:
#     print("Invalid OTP.")
    
# def func(n):
#     product = 1
#     if n == 0:
#         return
#     for i in range(1, n+1):
#         product *= i
#     print(product)
# func(4)

# n = [1, 2, 3, 2, 68]
# res = []
# for i in range(len(n)-1, -1, -1):
#     res.append(n[i])
# print(res)

# n = [1, 2, 3, 2, 68]
# start = 2
# end = 4
# left = start
# right = end
# while left < right:
#     n[left], n[right] = n[right], n[left]
#     left += 1
#     right -= 1
# print(n)

# n = [1, 2, 3, 2, 68]
# def func(n, left, right):
#     if left >= right:
#         return
#     n[left], n[right] = n[right], n[left]
#     func(n, left+1, right-1)
# func(n, 1, 4)
# print(n)

# n = [2, 3, 1, 6, 4, 5]
# def func(n, left, right):
#     if  >= left:
#         return
# func(n, 0)

# n = [2, 20, 200]
# for i in range(len(n)):
#     for j in range(i + 1, len(n)):
#         if n[i] > n[j]:
#             n[i], n[j] = n[j], n[i]
# print(n[-1])

# n = [2, 1, 2, 5, 1, 9, 1]
# sum = 0
# for i in range(len(n)):
#     sum += n[i]
# print(sum)

# arr = [10, 20, 30, 40, 50]
# target = 30
# print(arr.index(target))

# arr = [10, 20, 30, 40, 50]
# target = 30
# for i in range(len(arr)):
#     if arr[i] == target:
#         print(i)
#         break

# arr = [1, 2, 3, 2, 2, 4, 4]
# target = 4
# count = 0
# for i in range(len(arr)):
#     if arr[i] == target:
#         count += 1
# print(count)

# arr = [1, 3, 4, 5, 2]
# for i in range(len(arr)):
#     for j in range(i + 1, len(arr)):
#         if arr[i] > arr[j]:
#             arr[i], arr[j] = arr[j], arr[i]
# print(arr[-2])

# arr = [1, 2, 2, 3, 4, 4, 5, 6, 6, 6, 9, 9]
# res = dict()
# for i in range(len(arr)):
#     num = arr[i]
#     res[num] = arr.count(num)
# print(list(res.keys()))
            
# arr = [18, 200, 10, 23]
# for i in range(len(arr)):
#     for j in range(i+1, len(arr)):
#         if arr[i] > arr[j]:
#             arr[i], arr[j] = arr[j], arr[i]
# print(arr[-1])

# s = "abcdef"
# words = ["a", "bb", "acd", "ace"]
# count = 0
# for i in range(len(words)):
#     word = words[i]
#     p1 = 0
#     p2 = 0
#     
#     while p1 < len(word) and p2 < len(s):
#         if word[p1] == s[p2]:
#             p1 += 1
#         p2 += 1
#     
#     if p1 == len(word):
#         count += 1
#         
# print(count)

# s = "abcde"
# words = "aa", "bcd", "cde"
# count = 0
# for i in range(len(words)):
#     word = words[i]
#     p1 = 0
#     p2 = 0
#     while p1 < len(word) and p2 < len(s):
#         if word[p1] == s[p2]:
#             p1 += 1
#         p2 += 1
#     
#     if p1 == len(word):
#         count += 1
# print(count)

# n = "yfghjb"
# res = ""
# for i in range(len(n) -1, -1, -1):
#     res += n[i]  
# print(res)

# n = [1, 2, 3, 5, 2]
# start = 0
# end = 2
# left = start
# right = end
# while left < right:
#     n[left], n[right] = n[right], n[left]
#     left += 1
#     right -= 1
# print(n)

# arr = [3, 2, 1, 9]
# count = 0
# left = 0
# for i in range(len(arr)):
#     left += 1
#     count += 1
# print(count)
#     or 
# target = arr[-1]
# print(arr.index(target) + 1)

# n = [2, 3, 4, 9]
# left = 0
# right = len(n) -1
# for i in range(len(n)//2):
#     n[left], n[right] = n[right], n[left]
#     left += 1
#     right -= 1
# print(n)
# n = [2, 3, 4, 9]
# left = 0
# right = len(n)-1
# while left < right:
#     n[left], n[right] = n[right], n[left]
#     left += 1
#     right -= 1
# print(n)

# n = [2, 2, 10, 9]
# for i in range(len(n)):
#     for j in range(i + 1, len(n)):
#         if n[i] > n[j]:
#             n[i], n[j] = n[j], n[i]
# print(n[-1])

# s = "abbacsa"
# n = len(s)
# longest = ""
# for i in range(n):
#     left = i
#     right = i
#     while left >= 0 and right < n and s[left] == s[right]:
#         if (right - left + 1) > len(longest):
#             longest = s[left: right +1]
#         left -= 1
#         right += 1
#     left = i
#     right = i + 1
#     while left >= 0 and right < n and s[left] == s[right]:
#         if (right - left + 1) > len(longest):
#             longest = s[left: right +1]
#         left -= 1
#         right += 1
# print(longest)

# n = [1, 2, 3, 7]
# target = 3
# print(n.index(target))

# def func(n):
#     if n <= 0:
#         return n
#     elif n == 1:
#         return n
#     else:
#         return func(n-1) + func(n-2)
# print(func(2))

# def func(n):
#     if n == 0 or n == 1:
#         return n
#     else:
#         return func(n-1) + func(n-2)
# print(func(1))
# n = [1, 2, 3, 4, 3, 4, 1]
# res = dict()
# for i in range(len(n)):
#     char = n[i]
#     res[char] = n.count(char)
# print(list(res.keys()))
# n = "785r20"
# res = "" 
# for i in range(len(n) -1, -1, -1):
#     res += n[i]
# print(res)

# n = [2, 1, 5, 7, 4, 8, 4]
# for i in range(len(n)):
#     for j in range(len(n)):
#         if n[i] < n[j]:
#             n[i], n[j] = n[j], n[i]
# print(n[-1])

# s = "aaaabadsc"
# n = len(s)
# longest = ""
# for i in range(n):
#     left = i
#     right = i
#     while left >= 0 and right < n and s[left] == s[right]:
#         if (right - left + 1) > len(longest):
#             longest = s[left: right + 1]
#         left -= 1
#         right += 1
#     left = i
#     right = i + 1
#     while left >= 0 and right < n and s[left] == s[right]:
#         if (right - left + 1) > len(longest):
#             longest = s[left: right + 1]
#         left -= 1
#         right += 1
# print(longest)

# n = [1, 2, 3]
# target = 2
# left = 0
# for i in range(len(n)):
#     left += 1
#     if left == target:
#         print(left-1)

# arr_time = []
# burst_time = []
# n = int(input("Enter number of process: "))
# for i in range(n):
#     at = int(input(f"Enter the Arrival Time for Process {i+1}: "))
#     bt = int(input(f"Enter the Burst Time for Process {i+1}: "))
#     arr_time.append(at)
#     burst_time.append(bt)
# print("\nP\tAT\tBT")
# for i in range(n):
#     print(f"P{i+1}\t{arr_time[i]}\t{burst_time[i]}")

# arr = [10, 2, 7, 1]
# for i in range(len(arr)):
#     for j in range(i+1, len(arr)):
#         if arr[i] > arr[j]:
#             arr[i], arr[j] = arr[j], arr[i]
# print(arr)
# 
# #Or
# 
# def func(arr):
#     n = len(arr)
#     for i in range(0, n):
#         min_index = i
#         for j in range(i+1,n):
#             if arr[j] < arr[min_index]:
#                 min_index = j
#         arr[i], arr[min_index] = arr[min_index], arr[i]
#     return arr
#     
# arr = [10, 2, 7, 1]
# print(func(arr))

# import turtle
# import colorsys
# 
# t = turtle.Turtle()
# s = turtle.Screen()
# s.bgcolor('black')
# t.speed(0)
# n = 50
# h = 0
# 
# for i in range(280):
#     c = colorsys.hsv_to_rgb(h, 1, 0.8)
#     h = h + 1/n
#     t.color(c)
#     t.forward(i*2)
#     t.left(145)
#     
# turle.done()

# n = 12121
# num = n
# res = 0
# while n>0:
#     digit = n % 10
#     res = res*10 + digit
#     n = n//10
# if num == res:
#     print("Palindrome.")
# else:
#     print("Not Palindrome.")
    
# arr = [10, 2, 4]
# n = len(arr)
# for i in range(n-2, -1, -1):
#     for j in range(0, i+1):
#         if arr[j] > arr[j+1]:
#             arr[j], arr[j+1] = arr[j+1], arr[j]
# print(arr)

# arr = [10, 2, 4]
# n = len(arr)
# for i in range(n):
#     for j in range(i+1, n):
#         if arr[i] > arr[j]:
#             arr[i], arr[j] = arr[j], arr[i]
# print(arr)

# arr = [10, 2, 4, 9, 5, 8]
# n = len(arr)
# for i in range(1, n):
#     key = arr[i]
#     j = i-1
#     while j >= 0 and arr[j] > key:
#         arr[j+1] = arr[j]
#         j -= 1
#     arr[j+1] = key
# print(arr)

# n = 6
# for i in range(1, n):
#     for j in range(1, i+1):
#         print("*", end = "")
#     print("\n")

# s = "aanasbsa"
# n = len(s)
# longest = ""
# for i in range(n):
#     left = i
#     right = i
#     while left >= 0 and right < n and s[left] == s[right]:
#         if (right - left + 1) > len(longest):
#             longest = s[left: right + 1]
#         left -= 1
#         right += 1
#     left = i
#     right = i + 1
#     while left >= 0 and right < n and s[left] == s[right]:
#         if (right - left + 1) > len(longest):
#             longest = s[left: right + 1]
#         left -= 1
#         right += 1
# print(longest)

# arr = [10, 2, 6, 20, 5, 8]
# start = 0
# end = 3
# left = start
# right = end
# while left < right:
#     arr[left], arr[right] = arr[right], arr[left]
#     left += 1
#     right -= 1
# print(arr)

# n = [1, 2, 3, 5, 2]
# start = 0
# end = 2
# left = start
# right = end
# while left < right:
#     n[left], n[right] = n[right], n[left]
#     left += 1
#     right -= 1
# print(n)

# count = 0
# def fac(n):
#     global count
#     for i in range(1, n+1):
#         if n%i == 0:
#             count += 1
#     if count > 2:
#         print("Not Prime.")
#     else:
#         print("It's Prime.")
# 
# fac(10)

# import random
# print("Simple OTP Generater...")
# generator = random.randint(1111, 9999)
# print("Your OTP: ", generator)
# n = int(input("Enter your OTP for verification: "))
# if n == generator:
#     print("Your OTP is verified.")
# else:
#     print("Error!! Wrong OTP.")
    
# arr = [1, 2, 5, 8]
# left = 0
# right = len(arr) -1
# while left < right:
#     arr[left], arr[right] = arr[right], arr[left]
#     left += 1
#     right -= 1
# res = []
# for i in range(len(arr)-1, -1, -1):
#     res.append(arr[i])
# print(res)

# def merge_array(left, right):
#     result = []
#     i, j = 0, 0
#     n, m = len(left), len(right)
#     while i<n and j<m:
#         if left[i] <= right[i]:
#             result.append(left[i])
#             i+=1
#         else:
#             result.append(right[j])
#             j+=1
#     if i<n:
#         while i<n:
#             result.append(left[i])
#             i+=1
#     if j<m:
#         while j<m:
#             result.append(right[j])
#             j+=1
#     print(result)
# merge_array([1, 2, 3, 4], [1, 1, 3, 4, 5, 6, 7])

# s = 148410
# n = s
# res = 0
# while s>0:
#     digit = s % 10
#     res = res*10 + digit
#     s = s//10
# if res == n:
#     print("Palindrome.")
# else:
#     print("Not Palindrome.")

# s = "abbasssacs"
# n = len(s)
# longest = ""
# for i in range(n):
#     left = i
#     right = i
#     while left >= 0 and right < n and s[left] == s[right]:
#         if (right - left + 1) > len(longest):
#             longest = s[left: right + 1]
#         left -= 1
#         right += 1
#     left = i
#     right = i+1
#     while left >= 0 and right < n and s[left] == s[right]:
#         if (right - left + 1) > len(longest):
#             longest = s[left: right + 1]
#         left -= 1
#         right += 1
# print(longest)

# def func(n):
#     if n == 0 or n == 1:
#         return n
#     else:
#         return func(n-1) + func(n-2)
# print(func(1))

# s = "abbabbasgh"
# n = len(s)
# longest = ""
# for i in range(n):
#     left = i
#     right = i
#     while left >= 0 and right < n and s[left] == s[right]:
#         if (right - left + 1) > len(longest):
#             longest = s[left: right + 1]
#         left -= 1
#         right += 1
#     left = i
#     right = i+1
#     while left >= 0 and right < n and s[left] == s[right]:
#         if (right - left + 1) > len(longest):
#             longest = s[left: right + 1]
#         left -= 1
#         right += 1
# print(longest)

# arr = [2, 1, 6, 10]
# for i in range(len(arr)):
#     for j in range(len(arr)):
#         if arr[i] < arr[j]:
#             arr[i], arr[j] = arr[j], arr[i]
# print("Largest: ", arr[-1])
# print("Smallest: ", arr[0])

# arr = [3, 5, 10]
# res = []
# arr.sort()
# for i in range(arr[0], arr[-1] + 1):
#     res.append(i)
# res = [x for x in res if x not in arr]
# print(res)

# arr = [1, 2, 2, 1, 6, 7, 7]
# res = {}
# for i in range(len(arr)):
#     n = arr[i]
#     res[n] = arr.count(n)
# result = []
# for key, value in res.items():
#     if value >= 2:
#         result.append(key)
# print(result)

# arr = [0, 2, 0, 1, 2, 50, 9, 0, 2]
# res = []
# res1 = []
# for i in range(len(arr)):
#     if arr[i] == 0:
#         res.append(arr[i])
#     if arr[i] != 0:
#         res1.append(arr[i])
# print(res1 + res)

# s = "hello"
# res = ""
# for i in range(len(s)-1, -1, -1):
#     res += s[i]
# if res == s:
#     print("Palindrome.")
# else:
#     print("Not Palindrome.")

# s = "abbabbasgh"
# res = {}
# for i in range(len(s)):
#     n = s[i]
#     res[n] = s.count(n)
# for key in res:
#     print(key, end = "")
# arr = [11, 20, 3, 1]
# for i in range(len(arr)):
#     for j in range(i + 1, len(arr)):
#         if arr[i] > arr[j]:
#             arr[i], arr[j] = arr[j], arr[i]
# print(arr)
# p = 5
# for i in range(p):
#     for j in range(i+1):
#         print(" * ", end = "")
#     print("\n")
# n = 4
# a = 8
# for i in range(n):
#     for j in range(a):
#         print(" * ", end = "")
#     print("\n")
# Longest Palindrome:
# s = "aba"
# n = s
# res = ""
# for i in range(len(s) -1, -1, -1):
#     res += s[i]
# if res == n:
#     print("Palindrome.")
# else:
#     print("Not Palindrome.")
# s = "121"
# n = s
# res = ""
# for i in range(len(s)-1, -1, -1):
#     res += s[i]
# if res == n:
#     print("Palindrome.")
# else:
#     print("Not Palindrome.")

# import numpy as np
# 
# a = np.array([[2, 4, 2], [3, 5, 1], [1, 6, 3]])
# b = np.array([[4, 0, 3], [1, 1, 2], [2, 3, 4]])
# 
# result = np.dot(a, b)
# 
# print("The matrix multiplication is: ")
# for row in result:
#     print(row)

# print("Simple Calculator...")
# op = input("Enter operator (+, -, *, /): ")
# a = float(input("Enter first number: "))
# b = float(input("Enter second number: "))
# if op == '+':
#     print(f"{a} + {b} = {a+b}")
# elif op == '-':
#     print(f"{a} - {b} = {a-b}")
# elif op == '*':
#     print(f"{a} * {b} = {a*b}")
# elif op == '/':
#     if a == 0:
#         print("Error! Divisible by zero is not possible.")
#     else:
#         print(f"{a} / {b} = {a/b}")

# arr = [0, 10, 2, 4, 1, 3, 3]
# res = {}
# ress = []
# for i in range(len(arr)):
#     n = arr[i]
#     res[n] = arr.count(n)
# for key, value in res.items():
#     if value == 1:
#         ress.append(key)
# print(ress)

# arr = [0, 200, 0, 1000, 60]
# res = []
# ress = []
# for i in range(len(arr)):
#     if arr[i] != 0:
#         res.append(arr[i])
#     else:
#         ress.append(arr[i])
# print(res + ress)

# #Reverse a string
# s = "abc"
# reverse = ""
# for i in range(len(s)-1, -1, -1):
#     reverse += s[i]
# print(reverse)
# 
# #Palindrome check
# s = "madam"
# copy_string = s
# reverse = ""
# for i in range(len(s)-1, -1, -1):
#     reverse += s[i]
# if reverse == copy_string:
#     print("True")
# else:
#     print("False")
#Return the first repeated alphabet
# s = "aabbcd"
# res = {}
# for i in range(len(s)):
#     n = s[i]
#     res[n] = res.get(n, 0) + 1
# for key, value in res.items():
#     if value == 1:
#         print(key)
#         break

# def fab(x):
#     if x == 0 or x == 1:
#         return x
#     else:
#         return fab(x-2) + fab(x-1)
# print(fab(7))

# s = "baab"
# res = {}
# for i in range(len(s)):
#     n = s[i]
#     res[n] = res.get(n, 0) + 1
# for key, value in res.items():
#     if value >= 2:
#         print(key)
# #         first_index = s.index(key)
# #         second_index = s.index(key, first_index + 1)
#         break
# # print(second_index)

# s = "baab"
# res = {}
# for i in range(len(s)):
#     n = s[i]
#     res[n] = res.get(n, 0) + 1
# for key, value in res.items():
#     if value >= 2:
#         print(key)
#         break

#1. Arrays...

#Find the largest and smallest element in an array
# arr = [121, 35, 1, 10, 34, 1, 0]
# Max = arr[0]
# Min = arr[0]
# for i in range(len(arr)):
#     if arr[i] > Max:
#         Max = arr[i]
#     elif arr[i] < Min:
#         Min = arr[i]
# print(Max, Min)

# Reverse an array
# arr = [12, 4, 35, 1, 34, 1, 45]
# left = 0
# right = len(arr) -1
# while left < right:
#     arr[left], arr[right] = arr[right], arr[left]
#     left += 1
#     right -= 1
# print(arr)
#or
# res = []
# for i in range(len(arr)-1, -1, -1):
#     res.append(arr[i])
# print(res)

#Find the second largest element
# def merge(arr):
#     if len(arr) == 1:
#         return arr
#     
#     mid = len(arr) // 2
#     left = merge(arr[:mid])
#     right = merge(arr[mid:])
#     
#     result = []
#     i = j = 0
#     
#     while i < len(left) and j < len(right):
#         if left[i] <= right[j]:
#             result.append(left[i])
#             i += 1
#         else:
#             result.append(right[j])
#             j += 1
#     result.extend(left[i:])
#     result.extend(right[j:])
#     
#     return result
# 
# arr = [12, 4, 35, 1, 34, 1, 45]
# arrr = merge(arr)
# print(arrr[-2])

#Check if array is sorted
# def merge(arr):
#     if len(arr) == 1:
#         return arr
#     
#     mid = len(arr) // 2
#     left = merge(arr[:mid])
#     right = merge(arr[mid:])
#     
#     result = []
#     i = j = 0
#     
#     while i < len(left) and j < len(right):
#         if left[i] <= right[j]:
#             result.append(left[i])
#             i += 1
#         else:
#             result.append(right[j])
#             j += 1
#     result.extend(left[i:])
#     result.extend(right[j:])
#     
#     return result
#             
# arr = [12, 4, 35, 1, 34, 1, 45]
# n = arr
# arrr = merge(arr)
# if arrr == n:
#     print("Sorted.")
# else:
#     print("Not Sorted.")

#Remove duplicates from sorted array
# arr = [2, 2, 3, 3, 6, 10, 10]
# res = {}
# for i in range(len(arr)):
#     n = arr[i]
#     res[n] = res.get(n, 0) + 1
# print(list(res.keys()))

#merge sort
# def merge(arr):
#     if len(arr) == 1:
#         return arr
#     mid = len(arr) // 2
#     left = merge(arr[:mid])
#     right = merge(arr[mid:])
#     
#     result = []
#     i = j = 0
#     
#     while i < len(left) and j < len(right):
#         if left[i] <= right[i]:
#             result.append(left[i])
#             i += 1
#         else:
#             result.append(right[j])
#             j += 1
#             
#     result.extend(left[i:])
#     result.extend(right[j:])
#     
#     return result

#Find the smallest and largest element in an array
# arr = [20, 20, 100, 100, 5, 700]
# Max = arr[0]
# Min = arr[0]
# for i in range(len(arr)):
#     if arr[i] > Max:
#         Max = arr[i]
#     elif arr[i] < Min:
#         Min = arr[i]
#         
# print(Max,",",Min )

# n = int(input("Enter a number: "))
# res = []
# for i in range(1, n+1):
#     if i % 3 == 0 and i % 5 == 0:
#         res.append("FizzBuzz")
#     elif i % 3 == 0:
#         res.append("Fizz")
#     elif i % 5 == 0:
#         res.append("Buzz")
#     else:
#         res.append(f"{i}")
# print('["' + '", "'.join(res) + '"]')

# low = 0
# high = 8
# n = (1+high)//2
# m = (low)//2
# print(n-m)

# res = []
# arr = [8, 1, 2, 2, 3]
# for i in arr:
#     c = 0
#     for j in arr:
#         if j<i:
#             c+=1
#     res.append(c)
# print(res)

# n = 121
# m = n
# c = 0
# while m>0:
#     val = m % 10
#     if n % val == 0:
#         c+=1
#     m//=10
# print(c)
# x = -10
# res = 0
# num = x
# while x>0:
#     digit = x % 10
#     res = res*10 + digit
#     x=x//10
# if num == res:
#     print("true")
# else:
#     print("false") 
        
# nums = [0,1,2,2,3,0,4,2]
# val = 2
# res = []
# ress = []
# c=0
# for i in nums:
#     if val!=i:
#         res.append(i)
#         c+=1
#     else:
#         ress.append("_")
# print(c)
# print(res)
# nums = [3,2,2,3]
# val = 3
# res = []
# ress = []
# k=0
# for i in nums:
#     if val!=i:
#         res.append(i)
#         k+=1
#     else:
#         ress.append("_")
# print(k)

# nums = [1, 1, 2]
# res = []
# k=0
# for i in range(len(nums)):
#     for j in range(i+1, len(nums)):
#         if nums[i] != nums[j]:
#             res.append(nums[i])
#             break
#             k+=1
#         i+=1
# print(res)

# n = 234
# num = n
# s=0
# p=1
# while num>0:
#     r = num%10
#     s+=r
#     p*=r
#     num=num//10
# print(p-s)

# arr = [2,3,5,1,3]
# extra = 3
# res = []
# c=0
# for i in range(len(arr)):
#     c+=1
#     arr[i] += extra
# arrr = arr
# for j in range(len(arrr)):
#     if arrr[j] >= c:
#         res.append("true")
#     else:
#         res.append("false")
# print(res)

# arr = [4,2,1,1,2]
# extra = 1
# res = []
# maxi = max(arr)
# for i in arr:
#     if (i+extra >= maxi):
#         res.append("true")
#     else:
#         res.append("false")
# print(res)

# nums1 = [1, 2, 3, 0, 0, 0]
# res = []
# m = 3
# nums2 = [2, 5, 6]
# n = 3
# for i in range(m):
#     res.append(nums1[i])
# for j in range(n):
#     res.append(nums2[j])
# res.sort()
# print(res)

# def fact(n):
#     if n==0:
#         return 1
#     return n*fact(n-1)
# print(fact(0))

# def func(n):
#     if n == 1 or n == 2:
#         return 1
#     elif n == 0:
#             return 0
#     a,b,c = 0,1,1
#     for i in range(3, n+1):
#         a,b,c = b,c,a + b + c
#     print(c)
# func(10000)

# n = int(input())
# arr = [n]
# arr = list(map(int, input("Enter the elements in array: ").split()))
# for i in range(len(arr)):
#     if arr[i] % 2 != 0:
#         print("0")
#         break
# else:
#     arr.sort()
#     print(arr[-1])

# n=100
# i=1
# while i<=n:
#     print(i, end=" ")
#     i*=2
# def func(i,n):
#     if n<i:
#         return
#     else:
#         func(i,n-1)
#         print(n, end=" ")
# func(1, 5)
# n = 100
# fact = 1
# for i in range(1, n+1):
#     fact*=i
# print(fact)

# def fact(n):
#     if n==0:
#         return 1
#     else:
#         return n*fact(n-1)
# print(fact(5))

# def fib(n):
#     if n == 0 or n == 1:
#         return n
#     else:
#         return fib(n-1) + fib(n-2) + fib(n-3)
# print(fib(8))

# n = 36
# count = 0
# 
# if n == 0:
#     print("false")
# elif n == 1:
#     print("true")
# else:
#     while True:
#         count += 1
#         if 2**count == n:
#             print("true")
#             break
#         elif 2**count > n:
#             print("false")
#             break

# def func(a, b):
#     if b == 0:
#         return a
#     return func(b, a%b)
# print(func(15, 20))
# x=2
# n=10
# for i in range(1, n+1):
#     res = x**i
# print(res)

# a = (2, 1, 4, 2)
# a[3] = 10
# a[1] = 99
# print(a)

# name = "abhi"
# print(type(name))
# 
# names = ["aman", "ravi", "sam"]
# print(type(names))
# 
# namess = ("raghu", "rahul", "ram")
# print(type(namess))

# arr = [3, 2, 1, 6]
# Max = arr[0]
# Min = arr[0]
# for i in range(len(arr)):
#     if arr[i] > Max:
#         Max = arr[i]
#     elif arr[i] < Min:
#         Min = arr[i]
# print(Max, Min)  

# arr = [2, 4, 5, 5, 2]
# res = []
# for i in range(len(arr)-1, -1, -1):
#     res.append(arr[i])
# print(res)

# nums = [1, 2, 3, 4]
# res = []
# res.append(nums[0])
# 
# for i in range(1, len(nums)):
#     x = res[i-1] + nums[i]
#     res.append(x)
# print(res)

# head = [1,1,1,2,3]
# res = {}
# ans = []
# for i in range(len(head)):
#     n = head[i]
#     res[n] = res.get(n, 0) + 1
# for key, value in res.items():
#     if value < 2:
#         ans.append(key)
# print(ans)
# nums = [0]
# 
# n = len(nums)
# res = []
# ress = []       
# for i in range(n):
#     if nums[i] % 2 == 0:
#         res.append(nums[i])
#     else:
#         ress.append(nums[i])
# print(res+ress)
# nums = [16, 17, 4, 3, 5, 2]
# max_val = nums[-1]
# ans = []
# for i in range(len(nums) -1, -1, -1):
#     if nums[i] >= max_val:
#         ans.append(nums[i])
#         max_val = nums[i]
# print(ans)

# left = 0
# right = len(nums) -1
# while left <= right:
#     mid = (left + right) // 2
#     
#     if nums[mid] == target:
#         return mid
#     elif nums[mid] < target:
#         left = mid + 1
#     else:
#         right = mid - 1
# return left
# arr = [2, 1, 1]
# # value = 0
# # while value in arr:
# #     value += 1
# # print(value)
# res = {}
# for i in range(len(arr)):
#     n = arr[i]
#     res[n] = res.get(n, 0) +1
# for key, value in res.items():
#     if value >= 2:
#         print("true")
#     else:
#         print("false")

# digits = [2, 4]
# res = digits[-1]
# ans = res + 1
# print(digits + ans)

# chars = "()())()"
# stack = []
# to_remove = [False] * len(chars)
# for i in range(len(chars)):
#     if chars[i] == '(':
#         stack.append(i)
#     elif chars[i] == ')':
#             if stack:
#                 stack.pop()
#             else:
#                 to_remove[i] = True
# 
# while stack:
#     to_remove[stack.pop()] = True
#     
# res = ""
# for i in range(len(chars)):
#     if not to_remove[i]:
#         res += chars[i]
# print(res)

# arr = [1, 2, 3, 40, 5]
# s = 0
# for i in range(len(arr)):
#     s += arr[i]
# print(s)

# s = "abaaba"
# res = ""
# for i in range(len(s)-1, -1, -1):
#     res += s[i]
# if res == s:
#     print("Palindrome.")
# else:
#     print("Not Palindrome.")
    
temp = [30, 40, 38, 44]
n = len(temp)
start = 0
i = 0
count = 0
res = []
while i >= start:
    if temp[start] < temp[i]:
        count += 1
        res.append(start, count)
        count = 0
        start += 1
        i = start
    else:
        count += 1
        i += 1
        

    
# for i in range(1, n):
#     if start < temp[i]:
#         count += 1
#         res.append(count)
#         count = 0
#         start += 1
#     if n == i + 1:
#         res.append(0)
#     else:
#         count += 1
print(res) 
    
