# You can compare List Objects by using comparison operator

# <, >, <=, >=, ==, !=

# However, you can only use ==, != with List Operators

# Comparison is done only on 3 points
# 1. number of elements
# 2. content of elements - thi is case-sensitive
# 3. order of elements

a = [1, 2, 3]
b = [4, 5, 6]
c = [1, 2, 4]
d = [1, 2, 3]
e = [1, 3, 2]

print(a == b)
print(a == c)
print(a == d)
print(a == e)

# two list with strings

x = ["python", "programming"]
y = ["PYTHON", "PROGRAMMING"]
z = ["python", "programming"]

print(x == y)
print(y == z)
print(x == z)
