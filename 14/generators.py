def cube():
    for i in range(50):
        yield i ** 3

iterator = cube()

for i in iterator:
    print(i)

# print(next(iterator))