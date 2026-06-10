def ascii(input):
    result=""
    for char in input:
        if ord(char)%2==0:
            result+=char.upper()
        else:
            result+=char.lower()
    return result
print(ascii("newtons institute of engineering"))
