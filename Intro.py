# variables and data types

# message = "hello world"
# print(message)
# message = "new message"
# print(message)
#
# name = "jon phillips"
# print(name.title())
# # .title() capitalizes first letter in new words
#
# print(name.upper())
# print(name.lower())
#
# firstName = "jon"
# lastName = "phillips"
# fullName = f"{firstName} {lastName}"
# print(fullName)
# # f-strings - f is for format
#
# print(f"Hello, {fullName.title()}!")
# # title still works here
#
# # this format will also work
# full_name = "{} {}".format(firstName, lastName)
# print(full_name.title())
#
# # new lines
# print("Languages:\nPython\nC\nJavaScript")
# # tabs
# print("Languages:\tPython\tC\tJavaScript")
# # new lines and tabs
# print("Languages:\n\tPython\n\tC\n\tJavaScript")

favorite_language = " python "
print(favorite_language.rstrip())  # strips the whitespace at the end of a string
print(favorite_language.lstrip())  # strips the whitespace in the front of a string
print(favorite_language.strip())   # strips all whitespace at front and end of string

message = "One of Python's strengths is its diverse community."
print(message)

# message = 'One of Python's strengths is its diverse community.'
# ^ does not work due to opening and closing with single quote

# v this will work because the \' cancels the closing of the string
message = 'One of Python\'s strengths is its diverse community.'
print(message)

# 3 ** 3 = 27 --> exponents 3 ** 2 = 9
print(3 ** 2)

# order of operations
# 14
print(2 + 3 * 4)

# 20
print((2 + 3) * 4)

# floats
print(0.1 + 0.1)

# 0.30000000000000004
print(0.2 + 0.1)
# 0.30000000000000004
print(3 * 0.1)

# When you divide any two numbers, even if they are integers that result in a
#   whole number, you'll always get a float
# 4/2 = 2.0
print(4/2)

# When writing long numbers, you can group digits with underscores
long_number = 14_000_000_000

# 14000000000
print(long_number)

# you can assign values to more than one variable using one line
x, y, z = 1, 2, 3
# y = 2
print(y)

# python does not have built-in constant types but developers use all capital letters
#   to indicate a constant not to be changed

MAX_CONNECTIONS = 5000


