def duplicates(input):
    count={}
    duplicates=[]
    for i in input:
      if i in count:
        count[i]+=1
      else:
        count[i]=1
    for i,counting in count.items():
        if counting>1:
            duplicates.append(i)
    return duplicates
input="vasavi radhika"
duplicate_char=duplicates(input)
print("Duplicate characters:", duplicate_char)


    
