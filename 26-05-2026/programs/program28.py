def recu(n):
 if n==1:
     return n
 else:
      return n*recu(n-1)
num=int(input("enter n value"))
if num<0:
    print("negative numbers are not eligible")
elif num==0:
    print("the factorial value is 1")
else:
    print(recu(num))
