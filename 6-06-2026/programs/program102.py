def filter(list):
    result=[]
    for i in list:
        if  isinstance(i,int) and i>=0:
            result.append(i)
    return result
print(filter([1,2,"d","g"]))
print(filter(["H","fg",2,3]))
