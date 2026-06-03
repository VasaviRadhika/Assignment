def greater(words,k):
    result=[]
    for i in words:
       if len(i)>k:
         result.append(i)
    return result
word_list=["apple","banana","grapes","guava"]
k=5
long_words=greater(word_list,k)
print(f"Words longer than {k} characters: {long_words}")
