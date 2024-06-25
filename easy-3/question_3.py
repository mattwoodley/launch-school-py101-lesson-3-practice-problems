# What will the following code output?

str1 = "hello there"
str2 = str1
str2 = "goodbye!"
print(str1) # Strings are immutable so str1 still points to the value "hello there" and therefore print(str1) prints "hello there".
# str2 pointed to the same location in memory as str1 until it then reassigned str2 to "goodbye!", at that point it pointed to the new location in memory that "goodbye!" was assigned to

# Try to answer without running the code.