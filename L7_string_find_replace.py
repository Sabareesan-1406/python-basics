# searching a smaller string in a larger string and replace it

string_a = "ABCDE+++FGHIJ"

sub_String = "+"
print(f"old string - {string_a}")

new_string = string_a.replace("+", "x")
print(f"new string - {new_string}")
