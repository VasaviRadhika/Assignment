def multiply(n):
    nums=[int(num) for num in n.split(",")]
    result=1
    for num in nums:
        result*=num
    return result
print(multiply("2,4"))
