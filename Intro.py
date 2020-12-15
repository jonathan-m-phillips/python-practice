# variables and data types

message = "hello world"
print(message)
message = "new message"
print(message)

name = "jon phillips"
print(name.title())
# .title() capitalizes first letter in new words

print(name.upper())
print(name.lower())

firstName = "jon"
lastName = "phillips"
fullName = f"{firstName} {lastName}"
print(fullName)
# f-strings - f is for format

print(f"Hello, {fullName.title()}!")
# title still works here

# this format will also work
full_name = "{} {}".format(firstName, lastName)
print(full_name.title())

# new lines
print("Languages:\nPython\nC\nJavaScript")
# tabs
print("Languages:\tPython\tC\tJavaScript")
# new lines and tabs
print("Languages:\n\tPython\n\tC\n\tJavaScript")
