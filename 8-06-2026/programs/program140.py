def vow(string,vowel):
    vowels="aeiouAEIOU"
    result=""
    for char in string:
        if char in vowels:
             result += vowel
        else:
             result += char
    return result
print(vow("apples","u"))
