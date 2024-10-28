"""
Ask the user for their age and then calculate and print their age in dog's years.
"""
user_age = int(input("Please enter your age:"))
dog_years = user_age * 7
print(f"Your are {dog_years} in dog years")

"""
Write a program that gets 2 numbers from the user for the sides of a rectangle,
calculates its area P (perimeter) and prints the result to the console/terminal.
"""
num1 = float(input())
num2 = float(input())

perimeter = num1 * num2

print(perimeter)

"""
Get a number from the user, check and print that the number is positive, 
negative, or zero
"""
num = float(input())
if num > 0:
    print("Number is positive")
elif num < 0:
    print("Number is negative")
else:
    print("Zero")
