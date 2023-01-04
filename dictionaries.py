"""
Dictionary
----------
* Key-value pair
* Enclosed by curly braces
"""

# my_dict is a dictionary
my_dict = {
    # name is a key, and Viraz is the value 
    "name": "Viraz",
    # fav_fruit is the key, and Apple is the value
    "fav_fruit": "Apple",
}

print(my_dict['name'])
print(my_dict["fav_fruit"])


my_dict = {'my_key': 'my_value'}
print(my_dict['my_key'])


my_dict = {'name': 'viraz', 'fav_fruit': 'apple', 'fav_animal': 'dog', 'fav_place': 'chitwan', 'age': 26}
print(my_dict)

my_dict = {
    'name': 'viraz', 
    'fav_fruit': 'apple', 
    'fav_animal': 'dog', 
    'fav_place': 'chitwan', 
    'age': 26
}
print(my_dict)


# Accessing value using its key
print(my_dict['name'])  # name is the key
print(my_dict['age'])  # age is the key
# or
print(my_dict.get('name'))
print(my_dict.get('age'))
print(my_dict.get('a_key_that_does_not_exists'))  # ==> returns None

# Print all the keys available in a dictionary
print(my_dict.keys())

# Remove an item (key-value pair) using its key
print(my_dict.pop('name'))
print(my_dict)

# Remove the last item and return the key-value as tuple
print(my_dict.popitem())
print(my_dict)

# Update the dictionary (add item or change value of the item)
my_dict.update({'name': 'Prasant'})  # Adds an item
print(my_dict)
my_dict.update({'name': 'Viraz'})  # Update the item
print(my_dict)

