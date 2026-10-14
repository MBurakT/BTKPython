square = lambda num: num ** 2

numbers = [1, 3, 5, 9]

result = list(map(square, numbers))
# result = list(map(lambda num: num ** 2, numbers))

print(square(3))
print(result)
print()

check_even = lambda num: num % 2 == 0

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

result = list(filter(check_even, numbers))
# result = list(filter(lambda num: num % 2 == 0, numbers))

print(check_even(5))
print(result)
print()