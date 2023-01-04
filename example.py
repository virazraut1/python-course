my_list = [1, 2, 3, 4, 5, 6, 7, 7, 8, 8, 8, 9, 9, 9, 9, 9, 9, 9]


print(my_list)

print(my_list[0])

print(my_list[-1])

my_list.append(3)
print(my_list)

item = 9
print(my_list.count(item))

index = 7
my_list.insert(index, 7)
print(my_list)

my_list.remove(9)
print(my_list)

print(len(my_list))

index = 4
remove_item = my_list.pop(index)
print(my_list)
print(f"item at index {index} is removed: {remove_item}")


