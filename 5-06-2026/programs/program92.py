def stutter(word):
    if len(word)<2:
        return "the word must contain  more than 2 letters"
    words=f"{word[:2]}.... {word[:2]}... {word}?"
    return words
print(stutter("Is"))
print(stutter("python"))
print(stutter("programming"))

