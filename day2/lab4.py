 # Nstudents take K apples and distribute them among each other evenly. The remaining
# (the indivisible) part remains in the basket. How many apples will each single student
# get? How many apples will remain in the basket? The program reads the numbers N and
# K. It should print the two answers for the questions above.

students = int(input("Enter the number of students?"))
apple = int(input("Enter the number of apples?"))
a = apple // students
b = apple % students
print(f"Apple each studets will get :{a} ")
print(f"Apple remain in the basket :{b} ")