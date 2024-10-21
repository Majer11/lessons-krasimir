# float(value_param) - turn the value_param to type float if possible
# age = float(input("Please enter your age: "))
# print(type(age))

# print("some print")
# print(age >= 18)

# if age >= 18:
#     # the block of code inside the if is executed/ran only if the condition is True
#     print("You can vote.")
#     print("Yay!")
# else:
#     # the block of code inside the else is executed/ran only if the condition in the IF is False
#     print("You can't vote.")

# Elif statements are used to check multiple condition.
# If the preceding if statement's condition is False, the program checks the condition in the elif statement.
# Else statement is used for providing a default action when none of the if or elif conditions are True.

grade = 4

if grade >= 5.5:
    print("Otlichen")
elif grade >= 4.5:
    print("Mnogo dobur")
elif grade >= 3.5:
    print("Dobur")
elif grade >= 2.5:
    print("Sreden")
elif grade >= 2:
    print("Slab")    
else:
    print("Default print. Ocenkata ne otgovarqshe na kriteriite")

print("Ocenkata e napisana")