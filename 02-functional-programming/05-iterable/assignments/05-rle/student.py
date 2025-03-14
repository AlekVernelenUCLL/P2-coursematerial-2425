def rle_decode(data):
    first = True
    count = 0
    for i, item in enumerate(data):
        if not first:
            previous_item = data[i-1]
        else:
            previous_item = item
            first = False

        if item == previous_item:
            count += 1
        else:
            