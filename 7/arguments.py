def changeName(n):
    n = "ada"

name = "yiğit"

changeName(name)

print(name)
print()

def change(n):
    n[0] = "istanbul"

sehirler = ["ankara", "izmir"]

n = sehirler.copy()

change(n)

print(sehirler)
print(n)
print()

def add(*params):
    return sum(params)

print(add(10, 20))
print(add(10, 20, 30))
print(add(10, 20, 30, 40, 50, 60))
print()

def display(person = dict()):
    if person is None or not bool(person):
        print("Değer boş veya mevcut değil!")
        return None

    for x, y in person.items():
        print(f"{x}:{y}")

person = {
    "name": "Burak",
    "age": 30,
    "job": "Developer"
}

display(None)
display(person)
print()

def displayUser(**params):
    for key, value in params.items():
        print(f"{key}: {value}")

displayUser(name = "Burak", age = 30, city = "istanbul", phone = "1231231")
print()

def myfunc(a, b, *args, **kwargs):
    print(type(a), a)
    print(type(b), b)
    print(type(args), args)
    print(type(kwargs), kwargs)

myfunc("test", 20, 30, 40, 50, key1 = "value", key2 = "value2")
print()

