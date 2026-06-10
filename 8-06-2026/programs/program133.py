def unique(n):
    dict={}
    for num in n:
        if num in dict:
            dict[num]+=1
        else:
            dict[num]=1
    for num,count in dict.items():
        if count==1:
            return num
print(unique([1,2,1,2,3,3,3,1,9]))

