# DRY - Do not Repeat Yourself is a very important programming principle. It is important to build reusable pieces
# it keeps the program clean, easy to update,
# easy to organize and reduce the overall time taken to code in a large project

# functions is all about reusing a piece of logic in your code
def add(a, b):
    print(f"a = {a}, b = {b} , a+b ={a + b}")


add(100, 200)
add(600, 1000)


# functions that returns your result, You can use the returned value as part of the remaining program
def multiply(a, b):
    x = a * b
    return x


result = multiply(2.5, 4)
print(f"result = {result}")


# functions with default values for parameters
def divide(a=45, b=10):
    return a / b


result = divide()
print(f"result = {result}")


# functions that can return more than one value parameters
def math_ops(a, b):
    return multiply(a, b), divide(a, b)


# the returned values will be in a tuple.
result = math_ops(25, 25)
print(f"result = {result}")

# another way to access the tuple
prod, divid = math_ops(25, 25)
print(f"product = {prod}")
print(f"divid = {divid}")
