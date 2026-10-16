class Person:
    def __init__(self, name, year):
        if len(name) > 10:
            raise Exception("name alani fazla karakter içeriyor.")
        else:
            self.name = name

p = Person("Aliiiiiiiiiiii", 1990)