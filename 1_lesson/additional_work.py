""" 
Shopping
"""
item1 = input()
item2 = input()
item1_price = float(input())
item2_price = float(input())
item1_quantity = int(input())
item2_quantity = int(input())
shipping_costs = 10

item1_cost = item1_price * item1_quantity
item2_cost = item2_price * item2_quantity
total_cost = item1_cost + item2_cost + shipping_costs

if total_cost >= 100:
    shipping_costs = 0
    print(f"You will receive free shipping. Your total cost is {total_cost}lv.")
else:
    print(f"Your total cost is {total_cost}lv.")

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

if not user_pass:
    print("You didn't enter anything. Please enter your password: ")
    user_pass = input()

if user_pass == correct_pass:
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
