#montonic :it follows the seuence which is non increasing or decreasing
def monotonic(arr):
    increasing=decreasing=True
    for i in range(1,len(arr)):
        if arr[i]>arr[i-1]:
            decreasing=False
        elif arr[i]<arr[i-1]:
            increasing=False
    return increasing or decreasing
arr1=[1,2,3,4,5,6,7]
arr2=[3,2,1]
arr3=[2,6,9,1,4,5]
print("arr1 is monotonic:", monotonic(arr1))
print("arr2 is monotonic:", monotonic(arr2))
print("arr3 is monotonic:", monotonic(arr3))
