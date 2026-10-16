def greeting(name):
    print("Hello ", name)

# greeting("Ali")
# print(greeting)

sayHello = greeting

# print(sayHello)
# print(greeting)

del sayHello
print(greeting)