# Write a Python program to sum three given integers. However, if two or more values are equal sum will be zero.
a = int(input("Enter first integer?"))
b = int(input("Enter second integer?"))
c = int(input("Enter third  integer?"))
if (a==b==c) or (a==b) or (b==c) or(c==a):
     print ("the sum is 0.")
else:
     sum = a+b+c
     print("The sum of the given integers is",(sum))

