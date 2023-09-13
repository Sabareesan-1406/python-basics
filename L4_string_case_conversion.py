string_a = "ABCD"
# check if string is in uppercase
print("is string_a in uppercase : ", string_a.isupper())
# check if string is in lowercase
print("is string_a in lowercase : ", string_a.islower())

# converting upper case to lowercase
string_b = string_a.lower()
print("lowercase of string_a ", string_b)

# check if string is in uppercase
print("is string_b in uppercase : ", string_b.isupper())
# check if string is in lowercase
print("is string_b in lowercase : ", string_b.islower())


string_d = "abcDEFG"
# check if string is in uppercase, Since string has mixed upper and upper case, the results will be False
print("is string_d in uppercase : ", string_d.isupper())
# check if string is in lowercase, Since string has mixed upper and lower case, the results will be False
print("is string_d in lowercase : ", string_d.islower())

