# dictionary

my_dict = {
    0: {
        "name": "Viraz",
        "surname": "Raut",
        "address": "Chanauli"
    },
    1: {
        "name": "paris",
        "surname": "Thapaliya",
        "address": "Bhandara"
    },
    2: {
        "name": "prasant",
        "surname": "paudel",
        "address": "ramghat"
    }
}


length = len(my_dict.items())  # Number of items in the dictionary

print(length)

for i in range(length):
    item = my_dict[i]
    print(item['name'], item['surname'], item['address'])


for item in my_dict.items():
    print(item)

