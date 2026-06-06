def curzon(n):
    numerator=2**n+1
    denominator=2*n+1
    return numerator%denominator==0
print(curzon(1))
print(curzon(5))
    
