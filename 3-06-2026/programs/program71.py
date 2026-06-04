from collections import OrderedDict
data=[('b', 2), ('c', 3), ('d', 4)]
data.append(['a',1])
sort=sorted(data,key=lambda x:x[0])
a=OrderedDict(sort)
print(a)
