def split(arr,k):
    if k<=0 or k>=len(arr):
        return arr
    first=arr[:k]
    second=arr[k:]
    result=second+first
    return result
arr=[1,2,3,4,5]
k=3
result=split(arr,k)
print("original array:" ,arr)
print("array after splitting and adding:",result)

    
