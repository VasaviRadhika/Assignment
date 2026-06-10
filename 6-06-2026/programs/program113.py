def add_indexes(lst):
     return [int(i + val)for i, val in enumerate(lst)]
a=input("enter values: ")
lst=list(map(int,a.split()))
print(add_indexes(lst))
