def even(n):
    for num in range(n+1):
        if num%2==0:
            yield num
try:
    n=int(input("enter n value: "))
    result=even(n)
    print(','.join(map(str,result)))
except ValueError:
    print("invalid input")
