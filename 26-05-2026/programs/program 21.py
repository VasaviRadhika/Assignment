# sum of digits
n=int(input("enter n value"))
sum=0

while n>0:
    rem=n%10
    sum+=rem
    n=n//10
print(sum)
    
