# Python offers List data structure which is referred to as sequence

# Sequence is nothing but data structure where in data is stored in sequential format and can
# be accessed using index

# Here, is how a List is stored

#   [0]   [1]   [2]   [3]   [4]   [5] - Positive Indexing - used to print from left to right
#   1      2     3     4     5     6  - Every block has an index associated with it
#  [-6]  [-5]  [-4]  [-3]  [-2]  [-1] - Negative Indexing - used to print from right to left

# Properties of list - When should you use list data structures
# 1. Duplicate objects are allowed
# 2. Insertion order is preserved

# Index as backbone
# Allows you to differentiate between duplicate objects
# Preserves the insertion order of lists

"""Creating Lists"""
# Declaring a list object - There are two ways you can create a list object

# 1. Declare an empty List
a = []
print(a) # Nothing gets printed

# 2. Create a list that contains some predefined objects
a = [1, 2, 3, 4, 5, 6]
print(a)

# 3. Using split() function
s = "I love python programming"
a = s.split()
print(a)
print(type(a))

# 4. Using list() function
a = list(range(10, 20, 2))
print(a)

a = list(range(10, 20, 1))
print(a)

# 5. list of numbers
a = [1, 2, 3]
print(a)

# 6. list of strings
a = ["python", "programming"]
print(a)

# 7. list of mixed datatypes
a = [1, "a", 2, "b"]
print(a)

# 8. Nested lists
a = [1, 2, ["a", "b"]]
print(a)
print(a[0])
print(a[2][1])

# 9. Accessing elements of the list
a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(a[1])
print(a[-1])

# 10. using slice operator to access elements of the given list
# list_name[start: stop: step]

print(a[1: 10: 1])
print(a[1: 10: 2])

# whenever we skip step value, the default value is considered to be 1
print(a[1: 10])

# the stop value can also be skipped
print(a[1::2])

print(a[1: 500: 2]) # it will include the last number in the list

# we can also use negative values to return the values
print(a[9: 1: -2])
