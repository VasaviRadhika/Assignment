#quadratic equation
import math
a=int(input("enter a value:"))
b=int(input("enter b value:"))
c=int(input("enter c value:"))
disc=b**2-4*a*c
if disc>0:
    r1=-b+(math.sqrt(disc))/2*a
    r2=-b-(math.sqrt(disc))/2*a
    print(f"r1 value is:{r1}\n r2 value is:{r2}")
else:
    real=-b/2*a
    img=math.sqrt(abs(disc))/2*a
    print(f"r1:{real}+{img}i")
    print(f"r2:{real}-{img}i")

