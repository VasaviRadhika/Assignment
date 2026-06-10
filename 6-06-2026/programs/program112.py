def filter(n):
    items=n.split()
    return[int(i) for i in items if i.isdigit()]
n=input("enter the values: ")
print(filter(n))
