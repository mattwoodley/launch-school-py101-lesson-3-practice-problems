# What is the output of the following code?

answer = 42

def mess_with_it(some_number):
    return some_number + 8

new_answer = mess_with_it(answer)

print(answer - 8) # 34 (42 - 8)

# int is immutable so new_answer points to a different memory address than answer

print(id(answer))
print(id(new_answer))