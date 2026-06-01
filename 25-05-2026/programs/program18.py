#fibnacci series
n=int(input("enter n value"))
n1,n2=0,1
count=0
if n<=0:
    print("enter a valid number")
elif n==0:
    print("fibonacci series",{n})
    print(n1)
else:
    print("fibonacci series")
    while count<n:
         print(n1)
         a=n1+n2
         n1=n2
         n2=a
         count+=1
