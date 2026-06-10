def hamming(str1,str2):
    if len(str1)!=len(str2):
       return "The length of two strings must be equal"
    else:
        distance=0
        for i in range(len(str1)):
            if str1[i]!=str2[i]:
              distance+=1
        return distance
print(hamming("abcdef","abcdef"))
print(hamming("SAHDJHS","sahdjhs"))
