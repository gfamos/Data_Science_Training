"""3 Easy methods to traverse Python Lists"""
a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Using while loop
i = 0
while i < len(a):
    print(a[i])
    i = i + 1

# Using for loop
for i in a:
    print(i)

# Using range function - should in case we wanted to know the index position of all elements
n = len(a)
for i in range(n):
    print(i, " : ", a[i])