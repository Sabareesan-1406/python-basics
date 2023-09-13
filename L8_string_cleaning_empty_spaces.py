string_a = "    What a wonderful world \n "

# this is a formatted string, you can insert your variables and it will be automatically concatenated
print(f"string with newline and spaces - '{string_a}' ")

cleaned_string = string_a.lstrip()
print(f"cleaned string is - '{cleaned_string}' ")
