# Continue Statement helps a program looped jump to the next statement

# Example 1:

a = 5
while a:
    print(a)
    a = a - 1
    if a == 2:
        continue
    print("Remaining Statements are skipped and loops continues")
