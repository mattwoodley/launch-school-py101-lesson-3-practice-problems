# Write a one-liner to count the number of lower-case t characters in each of the following strings:

statement1 = "The Flintstones Rock!"
statement2 = "Easy come, easy go."

# I thought this was incorrect so I wrote the concatenated string as well
#print(statement1.count("t"))
#print(statement2.count("t"))

# wrote this because I misunderstood the "one-liner" part
print(f'{statement1} {statement2}'.count("t"))
