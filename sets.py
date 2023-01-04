"""
Sets in python

* Always starts from curly braces
* Set does not support duplicate items
* Set is always unordered (position of the items does not matter)
* Items in a set are not indexed

Set Operations:
There are three baseic operations in a set:
* Difference
* Intersection
* Union
All the other operations can be made by the combination of these three basic operations.

"""

set1 = {1, 2, 3, "apple", "banana", "mango", "orange"}
set2 = {3, 4, 5, "mango", "banana", "cherry"}
set3 = {3, 4, 5, "mango", "cherry", "flask", "bottle"}

"""
Differnce
"""
# Print items that are in set1 but not in set2
print(set1 - set2)
# or
print(set1.difference(set2))

# Print items that are in set2 but not in set1
print(set2 - set1) 
# or
print(set2.difference(set1))

"""
Intersection
"""
# Print items that are common set1, set2, and set3
print(set1.intersection(set2, set3))
# or
print(set2.intersection(set1, set3))
# or
print(set3.intersection(set2, set1))

"""
Union
"""
# Print all the items in set1, set2, and set3
print(set1.union(set2, set3))
# or ....


# Print items that are in set1 but not in set2 and set3
print(set1.difference(set2.union(set3)))


"""
Other Methods in a Set
"""
set1.add("Kivi")  # add an item "Kivi" to the set1
set1.discard("Kivi")  # Removes an element "Kivi" from the set1 if exists
set1.clear()  # Removes all the items in the set1

