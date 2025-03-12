def repeat(value):
    while True:
        yield value

iterator = repeat(5)

print(next(repeat(5)))
print(next(repeat(5)))
print(next(repeat(5)))
print(next(repeat(5)))
print(next(repeat(5)))