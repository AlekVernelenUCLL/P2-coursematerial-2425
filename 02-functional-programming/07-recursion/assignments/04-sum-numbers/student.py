def sum_numbers(number):
    text = str(abs(number))

    if len(text) == 1:
        return number
    return int(text[-1]) + sum_numbers(int(text[:-1]))

print(sum_numbers(129))