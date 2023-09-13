fruits = ["apple", "banana", "cherry"]
for x in fruits:
    print(x)
    if x == "banana":
        print("I will not stop the loop, we will print cherry")
        continue
        print("I will not be printed")
