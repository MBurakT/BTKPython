# global scope
x = "global x"

def function():
    # local scope
    x = "local x"
    print(x)

function()
print(x)
print()

name = "global name"

def changeName(new_name):
    name = new_name
    print(name)

changeName("local name")
print(name)
print()

name = "global string" # 3. öncelik

def greeting():
    name = "local string" # 2. öncelik

    def hello():
        name = "inner func string" # 1. öncelik
        print("hello", name)

    hello()

greeting()
print()

