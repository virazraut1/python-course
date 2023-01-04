# Write a function named "find_greatest".
# The function takes three numbers i.e a, b and c 
# Then returns the greatest number between them


def find_greater(a, b, c):
    if a > b:
        if a > c:
            return a
        else:
            return c
    else:
        return b

 
greater = find_greater(10, 20, 30)
print(greater)

greater = find_greater(30, 25, 15)
print(greater)

greater = find_greater(40, 35, 50)
print(greater)

