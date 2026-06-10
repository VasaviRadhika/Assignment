def move_end(list,element):
    count=list.count(element)
    list=[x for x in list if x!=element]
    list.extend([element]*count)
    return list
print(move_end([1,2,3,4,4,1,2],1))
