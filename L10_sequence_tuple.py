# a tuple is immutable sequence and it is indexed.

my_tuple = (0, 1, 2, 3)

# my_tuple.append is not allowed since tuple is immutable,  so you cannot add an element from tuple

# my_tuple.pop is not allowed since tuple is immutable, so you cannot remove an element from tuple
# my_tuple.sort is not allowed since tuple elements's order is also immutable

# you can use index to access specific element values from tuple.
print(f"value of element in index 2 = {my_tuple[2]} ")

# you can print the length of the tuple
print(f"length of my tuple = {len(my_tuple)}")

