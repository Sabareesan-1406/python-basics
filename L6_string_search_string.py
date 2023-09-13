# searching a smaller string in a larger string

string_a = "ABCDE FGHIJ"

# if the searched string is  found, the function returns the index at which the substring is found
index_found = string_a.find("D")
print("'D' is found  at position ", index_found, "in string_a")

# if the searched string is not found, the function returns -1
index_found = string_a.find("Z")
print("'Z' is found  at position ", index_found, "in string_a")

# if the searched string is not found, the function returns -1. Find has to match the entire sequence.
index_found = string_a.find("DEC")
print("'DEC' is found at position", index_found, "in string_a")

# if the searched string is case-sensitive so will return -1 if cases does not match.
index_found = string_a.find("d")
print("'d' is found  at position ", index_found, "in string_a")