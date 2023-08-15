"""VARIABLES IN PYTHON"""
# There are rules to keep in mind whilst creating these variables

total = 100 # Python is smart enough to identify the variable

print(total)

sum = total
print(sum)

print("sum : ", sum)

# Note also that variables can be re-assigned
sum = 1000
print(sum)

# You can create multiple variables and assign them same value
a = b = c = 10
print(a)
print(b)
print(c)

# Assign them to different values

a, b, c = 1, 2, 3 # What this does is that, it will first create three variables and then assign
print(a)
print(b)
print(c)

# Python also facilitate deleting variable
del sum
print(sum)

"""Rules To Keep in Mind"""
# Variable names should make sense
# Cannot start with digits
# Cannot contain special characters except underscore
# Variables with two words are usually separated using_to enhance readability

