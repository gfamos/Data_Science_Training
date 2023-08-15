# Python provides for a certain situation where you can execute a loop until a certain
# condition is met.

# while condition:
#   body - this, will be executed until the condition above is met

# Example 1: Writing a while loop that will print the value of variable until it reaches a certain
# value

a = 1
while a < 5: # While loop is executed until this condition is false
    print(a)
    a = a + 1
print("out of while loop")

# While loop is generally used when you are not aware of the number of iterations upfront

# While loop is executed till condition specified returns false

# Body of While loop is determined by the indentation

# You can use non-boolean value in place of condition, any non-zero value will be as True and
# 0 will be treated as False

# Example 2:
a = 1
while a: # While loop is executed until this condition is false
    print(a)
    a = a - 1
print("out of while loop")

# Example 3: while loop with else
a = 5
while a: # While loop is executed until this condition is false
    print(a)
    a = a - 1
else:
    print("out of while loop")