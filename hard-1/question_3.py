# Given the following similar sets of code, what will each code snippet print?

# A)
"""
def mess_with_vars(one, two, three):
    one = two
    two = three
    three = one

one = ["one"]
two = ["two"]
three = ["three"]

mess_with_vars(one, two, three)

print(f"one is: {one}") # ["one"]
print(f"two is: {two}") # ["two"]
print(f"three is: {three}") # ["three"]

# local variables so nothing is reassigned
"""





# B)
"""
def mess_with_vars(one, two, three):
    one = ["two"]
    two = ["three"]
    three = ["one"]

one = ["one"]
two = ["two"]
three = ["three"]

mess_with_vars(one, two, three)

print(f"one is: {one}") # ["one"]
print(f"two is: {two}") # ["two"]
print(f"three is: {three}") # ["three"]

# global variables cannot be reassigned
"""
# C)

def mess_with_vars(one, two, three):
    one[0] = "two"
    two[0] = "three"
    three[0] = "one"

one = ["one"]
two = ["two"]
three = ["three"]

mess_with_vars(one, two, three)

print(f"one is: {one}") # ["two"]
print(f"two is: {two}") # ["three"]
print(f"three is: {three}") # ["one"]

# lists are mutable and the mess_with_vars function has been given access to the lists through its parameters.
# you cannot reassign the variables themselves but as lists are mutable you can change the values within them.