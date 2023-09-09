# Python offers a break statement which can be used to exit a loop

# Example 1:
a = 5
while a:
    print(a)
    a= a - 1
    if a == 2:
        break
    print("while loop still meets condition")
print("Condition met")

# Example 2:
a = [1, 2, 3, 4, 5]
for i in a:
    print(i)
    if i == 3:
        break
    print("Last statement of for loop")
print("Outside for loop")
