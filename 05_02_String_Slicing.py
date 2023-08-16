# How can you use String Slicing to access the character of a given string?
# string_name[start_index: end_index: step]

a = "python"
print(a[1:4:1]) # returns yth
print(a[1:4:2]) # returns yh
print(a[1:4:]) # returns yth
print(a[1::]) # returns ython
print(a[:4:]) # By default, this will start at 0 - returns pyth
print(a[::2]) # returns pto
print(a[:4:2]) # returns pt
print(a[::]) # returns python
