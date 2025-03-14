def countX(text):
    if not text:
        return 0
    return (1 if text[0] == 'x' else 0) + countX(text[1:])


text = 'xhalxxxloxikxbxenxxblixjx'
print(countX(text))