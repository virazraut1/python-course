"""
Returning value from a function

* the value returned by a fucntion can be stored and used when required
"""

# Write a function named "find_greater".
# The function takes two numbers and
# returns the greater number between them

def find_greater(a, b):
    if a > b:
        return a
    else:
        return b


greater = find_greater(10, 20)
print(greater)

greater = find_greater(30, 25)
print(greater)
