"""Implicit Type Canversion"""

a = 2 + 2.0 #Output is of the Float DataType
print(a)
print(type(a))

# a = "python" + 2
# print(a) # this will error out, so we will have to consider Explicit Type Casting

"""Explicit Type Casting"""
# int(), float(), complex(), bool(), str()

# int()

print(int(10.5))
print(type(10.5))

# print(int(3 + 2j))
print(int("10"))
# print(int("one")) #this will throw an error as it is invalid for int()

# float()

print(float(10)) # Will return the output in terms of float
# print(float(10 + 3j)) # A complex type cannot be convert to float
print(float("200"))
# print(float("two")) # ValueError: could not convert string to float: 'two'

# complex()

print(complex(10))
print(complex(10.2))
print(complex(True))
print(complex(False))
print(complex("10"))
# print(complex("Python")) - complex() arg is a malformed string

# bool() - Used to convert any value to boolean type

print(bool(0))
print(bool(1))
print(bool(100.123))
print(bool(1 + 10j))
print(bool(0 + 0j))
print(bool("True"))
print(bool("true"))


# STR()

print(str(10))
print(str(10.5))