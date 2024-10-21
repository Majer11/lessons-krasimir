"""
input() function always returns a string
"""

# Comment on a single line

# name is variable of type string
name = input('Enter your name: ')
print("Hello,", name, ".How are you?")
print("Hello, " + name + ".How are you?") # with the + sign we do string concatenation
print(f"Hello, {name}. How are you?")

"""
def sum(a, b):
    return a + b

sum(5, 2)
sum(3, 4)
"""