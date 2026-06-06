a,b,c=map(int,input("enter a,b,c values:").split())
sum=0
for i in range(a,b+1):
    if i%c==0:
        sum=sum+i
print(sum)
