string_a = "ABCD"
string_b = "EFGH"
string_c = "abcd"

# Exercise 1
# let's compare string_a is same as string_b
is_same = (string_a == string_b)
print("string_a is same as string_b : ", is_same)
# output will be False

# Exercise 2
# string comparison is type sensitive, same alphabets with upper and lower case will not match
is_same = (string_a == string_c)
print("string_a is same as string_c : ", is_same)
# output will be False

# Exercise 3
# string comparison is type sensitive, same alphabets with upper and lower case will not match
string_d = string_a
is_same = (string_a == string_d)
print("string_a is same as string_d : ", is_same)
# output will be True

