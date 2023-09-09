# Why do we need for loop? For loop are used to iterate over sequence

# for x in sequence
#   body

# Example 1:
a = [1, 2, 3, 4, 5, 6]
print(type(a))

for x in a:
    print(x)

# for loop can also be used to iterate over strings;

# Example 2:
s = "I love Python"
for y in s:
    print(y)

# range()
for i in range(1, 10, 2):
    print(i)

# for loop with else
for x in a:
    print(x)
else:
    print("End")