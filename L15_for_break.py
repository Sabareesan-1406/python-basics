# break is used to break out of a loop

fruits = ["apple", "banana", "cherry"]
for x in fruits:
    print(x)
    if x == "banana":
        print("loop will break now, cherry is not printed")
        break
        print("this message will not be printed")
