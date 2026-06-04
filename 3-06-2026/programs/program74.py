import math
C=50
H=30
def calculate(D):
  return int(math.sqrt((2*C*D)/H))
Dval=input("enter D values : ").split(',')
result=[calculate(int(D)) for D in Dval]
print(','.join(map(str,result)))

