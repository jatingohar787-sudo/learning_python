import math
# this program calculates the area and circumferemce of a circle

radius = float(input("enter the radius of a circle : "))

circumference = (2 * math.pi * radius)

Area = (math.pi * pow(radius, 2))

print(f"the circumferedce of the circle is : {round(circumference, 2)}cm")

print(f"the area of the circle is : {round(Area, 2)}cm^2")
