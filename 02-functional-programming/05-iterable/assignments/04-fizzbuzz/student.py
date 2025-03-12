def fizzbuzz():
    counter = 1
    while True:
        if counter % 3 == 0:
            word = "fizz"
            if counter % 5 == 0:
                word = "fizzbuzz"
        elif counter % 5 == 0:
            word = "buzz"
        else:
            word = str(counter)
        yield word
        counter += 1
        

xs = fizzbuzz()

print(next(xs))
print(next(xs))
print(next(xs))
print(next(xs))
print(next(xs))
print(next(xs))