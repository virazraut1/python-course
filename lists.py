
my_list = ["potato", "tomato", "viraz", 2002, 2002, 3000]

print("Initial list:", my_list)

# Print first item of a list
print(my_list[0])

# Print last item of a list
print(my_list[-1])

# Add an item to the end of the list
my_list.append("Paris")
print(my_list)

# Add an item at any index
index = 4
my_list.insert(index, "Prasant")
print(my_list)

# Remove an item from a list (first occurance)
my_list.remove('Prasant')
print(my_list)

# Remove and return the last item from a list
last_item = my_list.pop()
print('Last item is removed from the list:', last_item)
print(my_list)

# Remove and return item at any index
index = 2
removed_item = my_list.pop(index)
print(f'Item at index {index} is removed: {removed_item}')

# Print number items in a list
print(len(my_list))

# Count the number of occurances in a list
item = 2002
print(my_list.count(item))

