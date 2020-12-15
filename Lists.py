

# bicycles = ['trek', 'cannondale', 'redline', 'specialized']
# # ['trek', 'cannondale', 'redline', 'specialized']
# print(bicycles)
#
# # trek
# print(bicycles[0])
#
# # Trek
# print(bicycles[0].title())
#
# # cannondale, specialized
# print(bicycles[1] + ", " + bicycles[3])
#
# # specialized
# print(bicycles[-1])
#
# message = f"My first bicycle was a {bicycles[0].title()}."
# # My first bicycle was a Trek.
# print(message)

# motorcycles = ['honda', 'yamaha', 'suzuki']
# ['honda', 'yamaha', 'suzuki']
# print(motorcycles)

# reassigning motorcycles[0]
# motorcycles[0] = 'ducati'
# # ['ducati', 'yamaha', 'suzuki']
# print(motorcycles)

# motorcycles.append('ducati')
# append adds ducati to the end of the list
# print(motorcycles)

# new_motorcycles = []
# new_motorcycles.append('honda')
# new_motorcycles.append('yamaha')
# new_motorcycles.append('suzuki')
# # ['honda', 'yamaha', 'suzuki']
# print(new_motorcycles)
#
# # insert(0, 'ducati') will inset ducati at the 0 index
# new_motorcycles.insert(0, 'ducati')
# # ['ducati', 'honda', 'yamaha', 'suzuki']
# print(new_motorcycles)
#
# # Removing an item using the del statement
# del new_motorcycles[0]
# # ['honda', 'yamaha', 'suzuki']
# print(new_motorcycles)
#
# del new_motorcycles[1]
# # ['honda', 'suzuki']
# print(new_motorcycles)

motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']

# Removing an item use pop
# ['honda', 'yamaha', 'suzuki', 'ducati']
print(motorcycles)

popped_motorcycles = motorcycles.pop()

# ['honda', 'yamaha', 'suzuki']
# print(motorcycles)

# ducati
print(popped_motorcycles)

# Pop takes the last item in the list and saves the item to popped_motorcycles
last_owned = motorcycles.pop()
print(f"The last motorcycle I owned was a {last_owned.title()}.")

# print(motorcycles)

motorcycles.append('ducati')
motorcycles.insert(2, 'suzuki')
# print(motorcycles)

# You can pop and item from a list if you know specific index - ex. pop(0)
first_owned = motorcycles.pop(0)

print(f"The first motorcycle I owned was a {first_owned.title()}.")

motorcycles.insert(0, 'honda')
# print(motorcycles)

# Removing an item by value
motorcycles.remove('ducati')
print(motorcycles)

motorcycles.append('ducati')

too_expensive = 'ducati'
# Removing an item using a variable
motorcycles.remove(too_expensive)

print(f"\nA {too_expensive.title()} is too expensive for me.")

