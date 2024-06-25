# Consider these two simple functions:
"""
def foo(param="no"):
    return "yes"

def bar(param="no"):
    return param == "no" and foo() or "no"

# What will the following function invocation return?

bar(foo())
"""
# False
# foo() returns "yes" as the parameter isn't used within the function body
# bar("yes") means that param == "no" is False and short-circuits so foo() isn't called. That just leaves False or "no" - "no" is truthy so  

print("yes" or "no")