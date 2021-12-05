# Given a positive real number, print its fractional part.
import math

a = float(input("enter a number?"))
x, y = math.modf(a)
print(x)
print(y)
