a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1]

# len() - It returns the length of a given list
print(len(a)) # you have the len and the list is pass as a parameter

# count() - It returns the count of the element in a given list
print(a.count(1))

# index() - It returns index for the first occurence of the specified element in a given list
print(a.index(3))

# sort() - It is used to sort a list in an ascending order
a.sort()
print(a)

# reverse() is the opposite of sort()
a.reverse()
print(a)
