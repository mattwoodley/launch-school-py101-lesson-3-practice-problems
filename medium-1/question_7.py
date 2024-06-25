# One day, Spot was playing with the Munster family's home computer, and he wrote a small program to mess with their demographic data:

munsters = {
    "Herman": {"age": 32, "gender": "male"},
    "Lily": {"age": 30, "gender": "female"},
    "Grandpa": {"age": 402, "gender": "male"},
    "Eddie": {"age": 10, "gender": "male"},
    "Marilyn": {"age": 23, "gender": "female"},
}

def mess_with_demographics(demo_dict):
    for key, value in demo_dict.items():
        value["age"] += 42
        value["gender"] = "other"

# After writing this function, he typed the following code:

mess_with_demographics(munsters)

# Before Grandpa could stop him, Spot hit the Enter key with his tail. Did the family's data get ransacked? Why or why not?

# Yes it does because dictionaries are mutable

print(munsters)
# I expect this to be:
"""
munsters = {
    "Herman": {"age": 74, "gender": "other"},
    "Lily": {"age": 72, "gender": "other"},
    "Grandpa": {"age": 444, "gender": "other"},
    "Eddie": {"age": 52, "gender": "other"},
    "Marilyn": {"age": 65, "gender": "other"},
}
"""

# Correct