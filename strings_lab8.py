# 1. STRING MANIPULATION USING STRING INPUT FROM USER


# coverts string to uppercase
user_input = input("Enter a string: ")
uppercase_string = user_input.upper()
print("Uppercase string:", uppercase_string)


# coverts string to lowercase
user_input = input("Enter a string: ")
lowercase_string = user_input.lower()
print("Lowercase string:", lowercase_string)

# reverses the string
user_input = input("Enter a string: ")
reversed_string = user_input[::-1]
print("Reversed string:", reversed_string)









#2. STRING SLICING AND INDEXING
a = input("Enter a string: ")

# print the first character
print("First character:", a[0])

# PRINTS LAST 2 CHARACTERS
print("Last two characters:", a[-2:])

# prints the string with every second character
print("String with every second character:", a[::2])

# reverse string without using slicing
user_input = input("Enter a string: ")
reversed_string = ""
for char in user_input:
    reversed_string = char + reversed_string
print("Reversed string:", reversed_string)










# 3. WORD FREQUENCY COUNTER 















# 4. remove punctuation from a string USING STRING MODULE OR STRING MOULE

