def equal(a,b,c):
    if a==b==c:
        return 3
    elif a==b or b==c or a==c:
        return 2
    else:
        return 0
a=int(input("enter a value: "))
b=int(input("enter b value: "))
c=int(input("enter c value: "))
print(equal(a,b,c))
