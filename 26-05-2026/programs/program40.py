name=input("enter names: ")
words = [word.capitalize() for word in name.split()]

words.sort()
for word in words:
 print(word)


