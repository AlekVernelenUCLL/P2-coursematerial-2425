from itertools import islice

def cycle(xs):
    while True:
        for item in xs:
            yield item

xs = cycle('abcd')

print(next(xs))
print(next(xs))
print(next(xs))
print(next(xs))
print(next(xs))