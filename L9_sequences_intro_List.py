"""
There are 3 different sequence / collection types in python
1. List / Array - mutable - uses [] to initialize
2. Tuple - immutable - uses () to initialize
3. Set - immutable , unindexed -  uses {} to initialize
"""

# A list of is the most commonly used sequence.
# Exercise 1 : list of integers
print(f" *** Exercise 1 : list of integers *** ")
# Following is a list of integers
int_list = [1, 2, -3, 4]
print(f"a = {int_list}")

# Exercise 2 : list of strings
print(f" *** Exercise 2 : list of strings *** ")
# Following is a list of strings
str_list = ["A", "eer", "asd", ]
print(f"b = {str_list}")

# Following is a mixed list os string and integer. However, it is  not a good practice to mix different datatypes in
# lists please avoid this in your programming
# Exercise 3 : list of mixed data
print(f" *** Exercise 3 : list of mixed data *** ")
mix_list = ["A", "eer", 3, 6]
print(f"c = {mix_list}")

# getting the length of the List
# Exercise 4 : length of the list
print(f" *** Exercise 4 : list of integers *** ")
print(f"length of int_list is - {len(int_list)}")

# getting an element of a list by index
# getting the element in the List by index
# Exercise 5 : getting the element in the List by index
"""
indexes in a sequences always start at 0
"""
print(f" *** Exercise  5: using index to access list elements *** ")
print(f"element at index 0 of list int_list - {int_list[0]}")
print(f"element at index 1 of list int_list - {int_list[1]}")
print(f"element at index 2 of list int_list - {int_list[2]}")
print(f"element at index 3 of list int_list - {int_list[3]}")

# you can also assign the value in the list to another variable without affecting the list
# assigning an element from list to another variable
# Exercise 6 : length of the list
x = int_list[3]
print(f" *** Exercise  6: using index to access list elements *** ")
print(f"value of x = {x}")

#  mutable in programming mean it can change
#  immutable in programming mean it cannot change
#  list is mutable and can be changed during the course of the program execution
#  Exercise  7: updating an element of a list using index
print(f" *** Exercise  7: updating an element of a list using index *** ")
my_list = [100, 200, 300, 400]
my_list[3] = "Z"
print(f"new updated list {my_list}")

#  Exercise  8: Maximum and Minimum indexes
print(f" *** Exercise  8: Maximum and Minimum index *** ")
"""
the maximum index of an list is always equal to its length - 1
minimum index is always 0
"""
string_list = ["a", "b", "c", "d", "e"]
# get the first element of a list - the first element has the smallest index - 0
print(f"first element of the string_list = {string_list[0]}")

max_index = len(string_list) - 1

print(f'the last index of the list string_list = {max_index}')
print(f'the last element in string_list = {string_list[max_index]}')

# adding a new element to the list
#  Exercise  9: adding or appending elements to an existing list
print(f" *** Exercise  9: adding or appending elements to an existing list *** ")
# this is an empty list , it has no elements. Its length is 0
new_list = []
# appending 3 new elements to the new_list
new_list.append(1000)
new_list.append(2000)
new_list.append(3000)
print(f"new_list = {new_list}")

# adding a new element to the list
# Exercise  10: adding or appending elements to an existing list
print(f" *** Exercise  9: removing elements from an existing list *** ")
list_a = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(f"list = {list_a}")
print("removing element at index 3")
list_a.pop(3)  # returns the poped element's value
# notice 3 is removed from the list.
print(f"updated list after removing element at index 3 = {list_a}")

# notice now 0 is removed. (3 was removed in previous step).
print("removing first element")
list_a.pop(0)  # returns the poped element's value
print(f"updated list after removing first and element at index 3 = {list_a}")

# notice now 9 is removed. (0 and 3 were removed in previous steps).
# To remove lst element , you dont have to provide index
print("removing last element")
list_a.pop()  # returns the poped element's value
print(f"updated list after removing last element, first and element at index 3 = {list_a}")

# Exercise  11: list elements can be sorted
a = [100, 400, 200, 300]
a.sort()  # returns a None Objects
print(f" *** Exercise  11:  elements in a list can be sorted *** ")
print(f"list after sorting in ascending order = {a}")

a.sort(reverse=True)
print(f"list after sorting in descending order = {a}")

# Exercise  12: index outside the maximum error.
print(f" *** Exercise  12:  index outside the maximum error *** ")

# if we use a index higher than the maximum index, then we will get an error - list index out of range
# the following statement will provide an index outside range error / exception
print(f'the last element in list a - {list_a[len(list_a)]}')
