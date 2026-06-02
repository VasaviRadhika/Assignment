#8^1+9^2=89
try:
    n=int(input("enter n value: "))
    s=sum(int(i)**(index+1) for index,i in enumerate(n)
    if s==n:
       print({n}, "is a disarium number")
    else:
        print({n},"is not adisarium number")
except ValueError:
    print("valid number")
          
