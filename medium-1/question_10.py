# In Python, every object has a unique identifier that can be accessed using the id() function. This function returns the identity of an object, which is guaranteed to be unique for the object's lifetime. For certain basic immutable data types like short strings or integers, Python might reuse the memory address for objects with the same value. This is known as "interning".

# Given the following code, predict the output:

a = 42
b = 42
c = a


print(id(a) == id(b) == id(c))


# Don't know how I'm supposed to know whether interning is happening or not based on "might"...

# id(a) could be the same as id(b) because their value is the same and so interning could happen, I guess
# Ignoring the idea that interning "might" happen, I'd say that they would be 2 different unique identifiers.
# interning or not I would expect id(c) to be equal to id(a) as they should be pointing to the same memory address

# If I assume interning is happening then that will print to True.

# Launch School's Answer says:

# In Python, there's a predefined range of integers, specifically from -5 to 256, for which memory locations are pre-assigned. When you reference an integer within this span, Python consistently points to the same memory spot. This strategy enhances efficiency since these particular numbers are commonly utilized in many programming scenarios.

# However, when you work with integers outside of this specific range, Python doesn't assure that it will consistently point to the same memory address for identical values across different variables.

d = 300

print(id(a)) # 140709698805464
print(id(b)) # 140709698805464
print(id(c)) # 140709698805464
print(id(d)) # 2149144174768