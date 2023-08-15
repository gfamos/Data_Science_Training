# There are 3 types of Flow Control; Conditional, transfer & Iterative
# 1. Conditional: Are used to execute certain piece of code based on certain condition;
# if
# else
# elif

# Example:
# if condition:
#   code to be executed

if 10 < 20:
    print("Hello Python")

# If the code about is reversed, you will NOT see anything in the result window because Python knows
# that 10 is NOT greater than 20

if 10 > 20:
    print("Hello Python")

age = 18
if age >= 18:
    print("Welcome to Facebook")

if 0: # Note that zero stands for False
    print("0 demo")

if 1: # Note that one stands for True
    print("0 demo") #Then, this line will get executed

# Example: There may be time you will like to execute series of code if the condition is False

# if condition:
#   code to be executed - if condition is True EXECUTE (True)
# else:
#   code to be executed - if condition is NOT True EXECUTE (False)

age = 18
if age >= 18:
    print("Welcome to Facebook")
else:
    print("You need to be 18 years old")

# Another Example:
age = 17
if age >= 18:
    print("Welcome to Facebook")
else:
    print("You need to be 18 years old")

# 2. Transfer:
# break
# continue
# pass

# 3. Iterative: perform repeatative set of action until certain conditions are met
# for
# while

