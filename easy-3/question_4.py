# What will the following code output?

my_list1 = [{"first": "value1"}, {"second": "value2"}, 3, 4, 5]
my_list2 = my_list1.copy()
my_list2[0]['first'] = 42
print(my_list1) # [{"first": 42}, {"second": "value2"}, 3, 4, 5]

# Try to answer without running the code.

#copy() returns a shallow copy, not a deep copy, and so any deeper levels than shallow won't be copied and will still point to the same object in memory, making them mutable