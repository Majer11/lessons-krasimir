num1 = float(input("Enter number 1: "))
num2 = float(input("Enter number 2: "))
num3 = float(input("Enter number 3: "))
# 3
# 2
# 1
max = num1
if num2 > max:
    max = num2
if num3 > max:
    max = num3

print(max)

# nested if statements
if num1 > num2:
    if num1 > num3:
        print(num1)
elif num2 > num1:
    if num2 > num3:
        print(num2)
else:
    print(num3)