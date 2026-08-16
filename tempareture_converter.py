# Temperature converter

unit = input("Celcius or Fahrenheit (C or F) : ")
temp = float(input("enter the tempareture : "))
if unit == "C" or unit == "c":
    temp = (temp * 9)/5+32
    print(f"The tempareture in fahrenheit is : {round(temp, 1)}F")
elif unit == "F" or unit == "f":
    temp = (temp - 32)*5/9
    print(f"The tempareture in Celcius is : {round(temp, 1)}C")
else:
    print(f"{unit} is invalid unit of measurement")
