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


