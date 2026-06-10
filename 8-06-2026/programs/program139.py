def map(letters):
    result={}
    for letter in letters:
        result[letter]=letter.upper()
    return result
print(map(["v","r"]))
