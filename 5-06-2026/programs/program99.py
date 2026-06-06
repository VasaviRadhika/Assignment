def replace(string,char):
    vowels="AEIOUaeiou"
    for vowels in vowels:
        string=string.replace(vowels,char)
    return string
print(replace("dafhdfgiuuoqwq","#"))
