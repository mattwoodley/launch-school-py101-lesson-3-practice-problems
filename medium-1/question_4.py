# What will the following two lines of code output?

print(0.3 + 0.6) # 0.9
print(0.3 + 0.6 == 0.9) # False - Something to do with how programming languages use floating-point numbers which means there's a degree of inaccuracy. I don't understand it better than that yet.

# Don't look at the solution before you answer.

# Launch school answer:
# 0.8999999999999999
# False

# Most floating point representations used on computers lack a certain amount of precision, and that can yield unexpected results like these.
# The details of why this happens aren't crucial right now -- it's just something you need to be aware of. One way around the problem is to use the math.isclose function: