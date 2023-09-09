# Does not do anything on execution but used to defined an empty block

# Example 1:
a = 5
while a:
    print(a)
    a = a - 1
    if a == 2:
        pass
    print("does nothing but conditions with empty block")


# Example 2:
a = 5
while a:
    pass