# Elif - Is the short form of Else If and used in different scenarios, where you will like to evaluate
# multiple scenarios;

# if condition:
#   Body of if
# elif condition:
#   Body of if elif
# else:
#   Body of else

# Example 1:
a = 3.4
if a > 0:
    print("This is positive number")
elif a == 0:
    print("This is zero")
else:
    print("This is negative number")

# Example 2:
a = -3.4
if a > 0:
    print("This is positive number")
elif a == 0:
    print("This is zero")
else:
    print("This is negative number")

# Example 3:
a = 0
if a > 0:
    print("This is positive number")
elif a == 0:
    print("This is zero")
else:
    print("This is negative number")

# Example 4:
a = 100
if a > 0 and a < 100:
    print("This is positive number")
elif a == 0:
    print("This is zero")
elif a > 100:
    print("Greater Than 100")
elif a < 100:
    print("Lesser Than 100")
else:
    print("This is negative number")

# Example 4:
a = 10000
if a > 0 and a < 100:
    print("This is positive number")
elif a == 0:
    print("This is zero")
elif "a > 100 and a < 1000":
    print("Greater Than 100")
elif a > 1000:
    print("Lesser Than 100")
else:
    print("This is negative number")

# Nested if Statement

# Example 5:
age = 18
if age > 18:
    if age > 60:
        print("Open Senior Citizen's Account")
    else:
        print("Open normal account")
    print("Open Account")
else:
    print("Not eligible")

# Example 6:
age = 61
if age > 18:
    if age > 60:
        print("Open Senior Citizen's Account")
    else:
        print("Open normal account")
else:
    print("Not eligible")
