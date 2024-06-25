# What do you think the following code will output?

nan_value = float("nan")

print(nan_value == float("nan"))

# I know that NaN is of type float but I don't understand more than that.
# I don't yet see why it wouldn't print as True

# Bonus Question
# How can you reliably test if a value is nan?
# math.isnan(value)
import math
print(type(nan_value))
print(math.isnan(nan_value))

# Launch School Answer
# The output is False. nan -- not a number -- is a special numeric value that indicates that an operation that was intended to return a number failed. Python doesn't let you use == to determine whether a value is nan.