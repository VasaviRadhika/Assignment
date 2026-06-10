def square(n):
    string=str(n)
    result=""
    for d in string:
        squared=int(d)**2
        result+=str(squared)
    return int(result)
print(square(6))
print(square(9))
        
