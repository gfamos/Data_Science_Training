# List are mutable - it is possible to update the values of list WITHOUT any new object being
# created in the background

# There are 2 fundamental ways of updating a list

a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]

# 1. Add new elements

# Using index to change the values
a[10] = 12
print(a)

# Using slicing operator to change the value
a[1: 4] = [33, 34, 35]
print(a)

a[1: 4] = [33, 34, 35, 36]
print(a)

a[1: 4] = [33, 34, 35, 36, 37] # this will NOT work because we have specified the end value as 4
print(a)

# Using append() function
a.append(200)
a.append(300)
print(a)

# Using extend() function
a.extend([2, 4, 6])
print(a)

# Using 2 new list to illustrate an example
b = [10, 20, 30]
c = [1, 2, 3]
c.extend(b)
print(c)

c.append(b)
print(c)

# Using insert() function
a.insert(2, 1)
print(a)

# 2. Delete elements
# Using del function
del a[1]
print(a)

# del function can also be used with range function
del a[1:3]
print(a)

# Using remove() - you can specify the element that you want to remove from a list
a.remove(5)
print(a)

# Range does not work with the remove element function
#a.remove(1:4)
print(a)

# Using pop() - used to remove an element specified in the parameter using index
a.pop(0)
print(a)

# if the index is not specified, it will remove the last element in the list
a.pop()
print(a)

# Using clear() - deletes all the element in a list
a.clear()
print(a)
