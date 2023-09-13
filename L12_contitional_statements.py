# If elif and else statement
# conditional statements in programming languages help us to make decisions by checking values of various operations.

# it is very important to keep your indentation clean and correct for conditional statements to work in python
a = 1
if a == 1:
    print("a=1")

# ***************  with an else statement, note else cannot take a comparator argument

b = 2
if b == 1:
    print("b=1")
else:
    print("b is not equal to 1")

# ***************  if elif and else statement

c = 50

if c == 2:
    print("c=2")
elif c == 5:
    print("c=5")
elif c == 50:
    print("c=50")
else:
    print("c=100")

# adding logical operators with if (AND/OR)

x = 100
y = 100

if (x == 100) and (y == 100):
    print("x and y = 100")

v = 200
s = 300
if (v == 200) and (s == 200):
    print("v and s = 200")
else:
    print("v and s are not equal to 200")
