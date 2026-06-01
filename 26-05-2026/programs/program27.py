def recursion(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return recursion(n-1) + recursion(n-2)

nterms = int(input("Enter n value: "))

if nterms <= 0:
    print("Please enter a positive number.")
else:
    print("Fibonacci terms:")
    for i in range(nterms):
        print(recursion(i))
