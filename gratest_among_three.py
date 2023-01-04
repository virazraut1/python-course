# Write a program to find the greatest number among three numbers
# assuming there is only one hightest number

a = 14
b = 12
c = 16


if a > b and a > c:
    print("A is the greatest")
elif b > a and b > c:
    print("B is the greatest")
else:
    print("C is the greatest")

# Nested if 
if a > b:
    if a > c:
        print("A is the greatest")
    if c > a:
        print("C is the greatest")
else:
    print("B is the greatest")
