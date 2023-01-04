# Nested dictionary

my_dict = {
    "viraz": {
        "name": "Viraz",
        "surname": "Raut",
        "address": "Chanauli"
    },
    "paris": {
        "surname": "Thapaliya",
        "address": "Bhandara"
    },
    "prasant": {
        "surname": "paudel",
        "address": "ramghat"
    }
}

print(my_dict['viraz']['surname'])  # viraz is a key, and surname is also a key
print(my_dict['viraz']['address'])
print(my_dict['prasant']['surname'])
print(my_dict['paris']['surname'])


person = my_dict['viraz']
print(person['name'])
print(person['surname'])
print(person['address'])
