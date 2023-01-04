"""
Passing values to the function
"""

# Write a function named "find_greater".
# The function takes two numbers and
# prints the greater number between them

def find_greater(a, b):
    if a > b:
        print(f"{a} is greater than {b}")
    else:
        print(f"{b} is greater than {a}")


find_greater(10, 50)
find_greater(30, 20)
find_greater(40, 22)