# python weight converter

Weight = float(input("enter your weight : "))
unit = input("Kilograms or Pounds (K or L): ")
if unit == "k" or unit == "K":
    Weight *= 2.205
    unit = " Lbs."
    print(f"your weight is : {Weight}{unit}")
elif unit == "L" or unit == "l":
    Weight /= 2.205
    unit = " Kgs."
    print(f"your weight is : {round(Weight, 2)}{unit}")
else :
    print(f"{unit} is not a valid unit.")