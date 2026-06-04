symbols=''''@#@$#Q#%$&^W&%&%&()%($+^_T{R^:R{:><>?"|'''
sentence=input("enter words: ")
contain=any(i in symbols for i in sentence)
if contain:
    print("the sentence contain symbols")
else:
    print("the sentence doesn't contain any special symbol")
