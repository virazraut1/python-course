# Write a program to keep asking for a number 
# until you enter a negative number. 
# At the end, print the sum of all entered numbers.

run = True
sum = 0

while run:

    num = int(input("Enter a number: "))

    # Add entered number to the sum
    sum += num

    # If number is negative, break the loop
    if num < 0:
        print("The sum of entered numbers is", sum)
        break

"""
Using for loop (maximum number of iterations = 20)
"""

sum = 0

for i in range(20):
    
    num = int(input("Enter a number: "))

    # Add entered number to the sum
    sum += num

    # If number is negative, break the loop
    if num < 0:
        print("The sum of entered numbers is", sum)
        break