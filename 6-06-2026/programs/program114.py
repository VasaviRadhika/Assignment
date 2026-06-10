import math
def cone(h,r):
    if r==0:
        return 0
    volume=(1/3)*math.pi*(r**2)*h
    return round(volume,2)
print(cone(1,2))
print(cone(1,0))
