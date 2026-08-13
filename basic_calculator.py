# BASIC CALCULATOR

operator = input("enter the operation to perform (+, -, *, /, %) : ")
num1 = float(input("enter a number : "))
num2 = float(input("enter a number : "))
if operator == "+":
    result = num1 + num2
    print(result)
elif operator == "-":
    result = num1 - num2
    print(result)
elif operator == "*":
    result = num1 * num2
    print(result)
elif operator == "/":
    result = num1 / num2
    print(result)
elif operator == "%":
    result = num1 % num2
    print(result)
else :
    print(f"{operator} is not a valid operator")
