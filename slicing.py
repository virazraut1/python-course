"""
List Slicing

>>> my_list[__start__:__end__]

where:  __start__ is the starting index
        __end__ is the last index

"""

my_list = ["apple", "banana", "mango", "strawberrry", "orange", "peach"]

print(my_list[2:])  # Slices from index 2 to end of the list
print(my_list[:2])  # Slices form start to index 2
print(my_list[2:-1])  # Slices from index 2 to second last
print(my_list[:-1]) # Slices from start to second last
print(my_list[-1:]) # Slices only the last element



name = 'Viraz'

# Slicing also works on strings
# because, string is the sequence (list) of characters
print(name[1:-1])
