name = 'Burak'
surname = 'Turhan'
age = 29

greeting = 'My name is ' + name + ' ' + surname + ' and \nI am ' + str(age) + ' years old'
length = len(greeting)

print(greeting)
print(greeting[0])
print(greeting[length - 1])
print(length)
print(greeting[-1])
print(greeting[3:7])
print(greeting[3:])
print(greeting[:16])
print(greeting[2:40:2])
print(greeting[2:40:3])