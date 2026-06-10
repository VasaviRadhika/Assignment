def mean(n):
    n_str=str(n)
    nsum=sum(int(digit) for digit in n_str)
    count=len(n_str)
    mean=nsum/count
    return int(nsum)
print(mean(123332734673))
