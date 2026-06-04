sentence = input("Enter a sentence: ")
print(sentence)
letter_count = 0
digit_count=0
for i in sentence:
    if i .isalpha():
        letter_count+=1

    elif i.isdigit():
        digit_count+=1
print( letter_count,"letters")
print(digit_count,"digits")
