# Tuple is a list of item but immutable

"""
* A tuple is enclosed by small braces
* The elements inside a tuple can not be added, changed or removed
* 
"""


my_tuple = ("potato", "tomato", "viraz", 2002, 3000)
print(type(my_tuple))

# Print first item
print(my_tuple[0])

# Print last item
print(my_tuple[-1])

# Count number of occurances of a item
item = 'viraz'
count = my_tuple.count(item)
print(f'Item = {item}, Count = {count}')


tuple1 = (1, 2, 3, 4, 5, 6, 6, 6, 6, 7)

print(tuple1.count(5))
print(tuple1.index(6))


