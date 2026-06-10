def triplet(a,b,c):
    sort=sorted([a,b,c])
    return sort[0]**2+sort[1]**2==sort[2]**2
print(triplet(1,2,3))
print(triplet(3,4,5))
