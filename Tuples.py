"""
Tuples cannot change the list so no functions like append, remove, clear, etc.
"""

numbers = (1,2,3)
print(numbers[0])

"""
Unpacking
"""

coordinates = (1,2,3)
x,y,z = coordinates
"""This is to assign each number to variables x,y,z"""
print(x)

"""Making dictionary"""

customer = {
    "name": "John Smith",
    "age": 30,
    "is_verified": True
}

print(customer["name"])
"or"
print(customer.get("name"))

customer["name"] = "Jack Smith"
print(customer["name"])

customer["birthdate"] = "24 June 1996"
print(customer["birthdate"])

"Exercise"
Numbers = input("Phone: ")
digits_mapping = {
    "1": "One",
    "2": "Two",
    "3": "Three",
    "4": "Four"
}
output = ""
for ch in Numbers:
    output += " " + digits_mapping.get(ch, "!")


print(output)

output = ""
for ch in Numbers:
    output += " " + digits_mapping[ch]

print(output)


