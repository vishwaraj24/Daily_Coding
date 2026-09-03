# String Data Type

name = input("Enter a string: ")
ch = input("Enter a character to find: ")

print("String =", name)
print("Data Type =", type(name))
print("Length =", len(name))
print("Uppercase =", name.upper())
print("Lowercase =", name.lower())

pos = name.find(ch)

if pos != -1:
    print("Position of", ch, "=", pos)
else:
    print("Character not found")