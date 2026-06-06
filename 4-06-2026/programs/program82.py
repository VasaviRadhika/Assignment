sentence=input("enter a sentence:").split()
words={}
for word in sentence:
    word=word.strip(',.!@#@##$#%$^%^%^%$')
    word=word.lower()
    if word in words:
        words[word]+=1
    else:
        words[word]=1
sorted_words=sorted(words.items())
for word,frequency in sorted_words:
    print(f"{word}:{frequency}")
        
    
