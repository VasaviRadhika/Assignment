def add(a,b):
  return a+b
def subtract(a,b):
  return a-b
def multiply(a,b):
  return a*b
def division(a,b):
  return a/b
print("1. addition")
print("2.subtraction")
print("3.multiplication")
print("4.division")
while True:
    choice=input("enter value:")
    if choice in ('1','2','3','4'):
        n1=float(input("enter n1 value"))
        n2=float(input("enter n2 value"))
        if choice=='1':
            print(add(n1,n2))
        elif choice=='2':
            print(subtract(n1,n2))
        elif choice=='3':
            print(multiply(n1,n2))
        elif choice=='4':
            if n2!=0:
                print(division(n1,n2)
            else:
                print("error")
                 
     else:
        print("invalid number")
        
