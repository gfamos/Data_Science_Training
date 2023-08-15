a = 10
b = 10
print(id(a)) # The address of the object created in the memory
print(id(b)) #Internally they point to the same memory location

b = 20
print(id(b)) # Note that the memory allocation changes