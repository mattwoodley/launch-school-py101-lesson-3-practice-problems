# Ben was tasked to write a simple Python function to determine whether an input string is an IP address using 4 dot-separated numbers, e.g., 10.4.5.11.

# Alyssa supplied Ben with a function named is_an_ip_number. It determines whether a string is a numeric string between 0 and 255 as required for IP numbers and asked Ben to use it. Here's the code that Ben wrote:

def is_an_ip_number(str):
    if str.isdigit():
        number = int(str)
        return 0 <= number <= 255
    return False

def is_dot_separated_ip_address(input_string):
    dot_separated_words = input_string.split(".")

    if len(dot_separated_words) != 4:
        return False

    while len(dot_separated_words) > 0: # Launch School did while dot_separated_words: Which is clever as it checks whether it is truthy or not based on whether its an empty list
        word = dot_separated_words.pop()
        if not is_an_ip_number(word):
            return False

    return True

print(is_dot_separated_ip_address("1.2.3.4"))
print(is_dot_separated_ip_address("10.4.5.11"))
print(is_dot_separated_ip_address("1.2.3.4.5"))
print(is_dot_separated_ip_address("10.4.5.300"))
print(is_dot_separated_ip_address("help"))

# Alyssa reviewed Ben's code and said, "It's a good start, but you missed a few things. You're not returning a false condition, and you're not handling the case when the input string has more or less than 4 components, e.g., 4.5.5 or 1.2.3.4.5: both those values should be invalid."

# Help Ben fix his code.