# class
class Person:
    # class attributes
    address = "no information"

    # constructor (yapıcı metod)
    def __init__(self, name, year):
        # object attributes
        self.name = name
        self.year = year
        print("init metodu çalıştı.")
    
    # methods
    def intro(self):
        print(f"Hello there. I am {self.name}")

    def calculateAge(self):
        return 2026 - self.year

# object (instance)
p1 = Person(name = "ali", year = 1990)
p2 = Person(name = "yağmur", year = 1995)

p1.intro()
p2.intro()

print(f"adım: {p1.name} ve yaşım: {p1.calculateAge()}")
print(f"adım: {p2.name} ve yaşım: {p2.calculateAge()}")
print()

