def happy_number(n):
    seen=set()
    while n!=1 and n not in seen:
      seen.add(n)
      n=sum(int(i)**2 for i in str(n))
    return n==1
n=int(input("enter a number: "))
if happy_number(n):
    print(f"{n} is a happy number")
else:
    print(f"{n} is not a happy number")

