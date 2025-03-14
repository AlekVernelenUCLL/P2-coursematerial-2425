def reverse_from_left(text):
    first_index = 0

    if first_index == len(text)-1:
        return text[first_index-1]
    elif text == "":
        return ""
    return reverse_from_left(text[first_index+1:]) + text[first_index]


def reverse_from_right(text):
    last_index = len(text)-1

    if last_index == 0:
        return text[last_index]
    elif text == "":
        return ""
    return text[last_index] + reverse_from_right(text[:last_index])

print(reverse_from_left('Hallo'))
print(reverse_from_right('1234'))