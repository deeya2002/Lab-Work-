# find BMI of a person where take mass and height as input from the user
# BMI=mass in kg / (height in m)2

m = int(input("enter the mass:"))
h = int(input("enter the height :"))
BMI = (m / (h*h))
print("the BMI of a person is {} kg\m\u00b2.".format(BMI))


