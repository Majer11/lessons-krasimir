"""
Daily time
"""
#time = int((input)("Please enter time in 0000 format: "))
time = 2200
if time >= 0000 and time < 1200:
    print('Good morning')
elif time >= 1200 and time < 1700:
    print("Good afternoon")
elif time >= 1700 and time < 2100:
    print("Good evening")
elif time >= 2100 and time < 2359:
    print("Good night")

"""
Correct pass
"""
correct_pass = "Lsss"

user_pass = input("Please enter your password: ")

if user_pass == input():
    print("You don't enter nothing. Please enter your password: ")
elif user_pass == correct_pass:
    print("Correct password")
else:
    print("Incorrect password")

"""
Even or odd number
"""
num = int(input())

if num % 2==0:
    print("Number is even")
else:
    print("Number is odd")

"""
Divisible number by 3
"""
num1 = int(input())

if num1 %3==0:
    print("The number is divisible by 3")
else:
    print("Not applicable")
