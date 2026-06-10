def index_caps(word):
    return [i for i,char in enumerate(word) if char.isupper()]
word=input("enter word: ")
print(index_caps(word))
