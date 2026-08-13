name = input("enter your name : ")
age = int(input("enter your age : "))
height = int(input("enter your height in cm : "))
height_in_meters = height / 100
weight = int(input("enter your weight in kg : "))
BMI = weight // height_in_meters**2
birth_year = 2026 - age
number_of_months_lived = age * 12
print(f"hellow {name}.")
print(
    f"your present age is {age} years old \nand you will be {age + 10} years old after 10 years")
print(
    f"your birth year is {birth_year} \nand according to your birth year you have lived approximatly {number_of_months_lived} months ")
print(f"your BMI value is {BMI}")


