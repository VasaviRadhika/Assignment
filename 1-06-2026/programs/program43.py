#8^1+9^2=89
def dissarium():
   n=input("enter n value: ")
   try:
    s=sum(int(i)**(index+1) for index,i in enumerate(n))
    n_val=int(n)
    if s==n_val:
       print({n_val}, "is a disarium number")
    else:
        print({n_val},"is not adisarium number")
   except ValueError:
    print("valid number")
dissarium()
          
