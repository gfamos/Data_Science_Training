"""Assessing String"""

# How can you access the characters of the strings?
# 1. Using Index:
#   0   1   2   3   4   5 - Positive Indexing - used to print from left to right
#   P   Y   T   H   O   N
#   -6  -5  -4  -3  -2  -1 - Negative Indexing - used to print from right to left

# Example 1.

a = "python"
print(a[0])
print(a[1])
print(a[2])
print(a[3])
print(a[4])
print(a[5])

# Example 2.

print(a[-6])
print(a[-5])
print(a[-4])
print(a[-3])
print(a[-2])
print(a[-1])

# Example 3. - length of the string - len()
print(len(a))

# Example 4. - Printing this way isn't convenient
i = 0
length = len(a)
while i < length:
    print(a[i])
    i = i + 1

# Example 5.
i = len(a) - 1
while i >= 0:
    print(a[i])
    i = i - 1

# 2. Using Slice Operator