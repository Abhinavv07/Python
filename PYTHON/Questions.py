# # inputting two numbers and printing their sum
# a = int(input("Enter first number :- "))
# b = int(input("Enter second number :- "))
#
# print("Sum of ", a, " and ", b, " is ", a + b)


# # Inputting side of square and printing its area
# side = int(input("Enter side :- "))
# print("Area of square :- ", side ** 2)

# # Inputting floating point number and printing their average
# num1 = float(input("Enter first number :- "))
# num2 = float(input("Enter first number :- "))
# print("Average of ", a, " and ", b, " is ", (a + b) / 2)

# # Checking greater number
# a = int(input("Enter first number :- "))
# b = int(input("Enter second number :- "))
# print(a >= b)

# # Grade students based on rank
# marks = int(input())
# if (marks >= 90):
#     grade = 'A'
# elif (marks < 90 and marks >= 80):
#     grade = 'B'
# elif (marks >= 70 and marks < 80):
#     grade = 'C'
# elif (marks < 70):
#     grade = 'D'
#
# print("Grade : ", grade)

# # Checking even or odd
# num = int(input("Enter number"))
#
# if (num % 2 == 0):
#     print("Even")
# else:
#     print("Odd")

# # Checking greatest of three number
# n1 = int(input("Enter first number"))
# n2 = int(input("Enter second number"))
# n3 = int(input("Enter third number"))
#
# if (n1 > n2 and n1 > n3):
#     print(n1, " is greatest")
# elif (n2 > n1 and n2 > n3):
#     print(n2, " is greatest")
# else:
#     print(n3, " is greatest")

# # Checking multiple of 7
# num = int(input())
#
# if (num % 7 == 0):
#     print("Multiple of 7")
# else:
#     print("Not a multiple of 7")

# Appending element
# movie = []
# mov1 = str(input("Enter first movie"))
# mov2 = str(input("Enter second movie"))
# mov3 = str(input("Enter third movie"))
#
# movie.append(mov1)
# movie.append(mov2)
# movie.append(mov3)
#
# print(movie)

# Printing 1 to 100
# i = 1
# while i <= 100:
#     print(i)
#     i+=1

# Printing from 100 to 1
# i = 100
# while i >= 1:
#     print(i)
#     i-=1

# Printing table of three
# n = 3
# i = 1
# while i <= 10:
#     print(n, " x ", i, " = ", (n*i))
#     i+=1

# printing elements of list using while loop
# l = [2,3,4,5,56,67,7,"akm"]
# i = 0
# while i < len(l):
#     print(l[i])
#     i+=1

# searching element in tuple
# t = (2,43,6,7,5,46,8)
# x = 6
# i = 0
# while i < len(t):
#     if(x == t[i]):
#         print("Element found")
#         break;
#     else:
#         print("Not found")
#         i+=1

# Printing elements of list using for loop
# li = [2,3,4,56,3,2,4,"Akxjvb"]
# for e in li:
#     print(e)

# Searching for a number in a tuple
# x = 13
# tup = (3,4,22,13,4,2,123)
# for e in tup:
#     if(x == e):
#         print("Found")
#     else:
#         print("Finding.....")

# Printing number from 1 to 100 using range()
# for i in range(1,101):
#     print(i)

# Printing number from 100 to 1
# for i in range(100,0,-1):
#     print(i)

# Printing table of 7
# for i in range(0,77,7):
#     print(i)

# program to print sum of first n numbers using while loop
# i = 1
# sum = 0
# while i <= 5:
#     sum += i
#     i += 1
# print(sum)

# Printing factorial of n
# fact = 1
# n = 5
# for i in range(1, n + 1):
#     fact *= i
#     print(fact)

# Program to print length of list using function
# list1 = [2, 43, 45, 4, 3, 345, 43, 2, 43, 34, 2, 4, 3, 4]
# def print_list(list):
#     print(len(list))

# def Print_list(list):
#     for item in list:
#         print(item, end=" ")
# print_list(list1)

# Printing factorial of n using function
# def facto(n):
#     fact = 1
#     for i in range(1,n+1):
#         fact *= i
#     return fact
#
# print(facto(4))

# Converting usd to inr
# def convert(usd):
#     return usd * 86
#
# print(convert(1))
