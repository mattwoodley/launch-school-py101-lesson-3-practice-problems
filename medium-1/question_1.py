# Let's do some "ASCII Art": a stone-age form of nerd artwork from back in the days before computers had video screens.

# For this practice problem, write a program that outputs The Flintstones Rock! 10 times, with each line prefixed by one more hyphen than the line above it. The output should start out like this:

"""
-The Flintstones Rock!
--The Flintstones Rock!
---The Flintstones Rock!
    ...
"""

sentence = "The Flintstones Rock!"
counter = 1

while counter in range(11):
    print(f'{counter * '-'}{sentence}')
    counter += 1

# launch school's solution uses the same idea but utilises a for loop and changes the name counter to padding