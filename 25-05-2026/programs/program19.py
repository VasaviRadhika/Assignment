#armstrong number
n=int(input())
l=len(str(n))
sum=0
temp=n
while n>0:
  rem=n%10
  sum=sum+rem**l
  n=n//10

if temp==sum:
  print("armstrong number")
else:
  print("not armstrong number")
