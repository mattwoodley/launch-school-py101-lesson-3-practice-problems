# Write two distinct ways of reversing the list without mutating the original list.

numbers = [1, 2, 3, 4, 5]     # [5, 4, 3, 2, 1]

print(numbers)
print(numbers[::-1])
print(sorted(numbers, reverse=True))
reversed_numbers = list(reversed(numbers))
print(reversed_numbers)
print(numbers)