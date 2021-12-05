# WAP which accepts marks of four subjects and display total marks, percentage and grade. Hint: more than 70% –> distinction, more than 60% –> first, more than 40% –> pass, less than 40% –> fail.
a =int(input("enter marks of programming and algorithm?"))
b = int(input("enter marks of software design?"))
c = int(input("enter marks of mathematics?"))
d = int(input("enter marks of Led computer project?"))
total = (a+b+c+d)
percentage = total/4
if percentage > 70:
  print ("Distinction")
elif percentage > 60:
  print ("First Division ")
elif percentage > 40:
  print ("Pass")
elif percentage < 40:
  print ("fail")
