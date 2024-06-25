# How can you determine whether a given string ends with an exclamation mark (!)? Write some code that prints True or False depending on whether the string ends with an exclamation mark.

str1 = "Come over here!"  # True
str2 = "What's up, Doc?"  # False

def exclamation(words):
    return words.endswith("!")

print(exclamation(str1))
print(exclamation(str2))
