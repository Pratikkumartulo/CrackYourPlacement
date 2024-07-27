def ceilSearch(arr,low,high,x):
    if x<=arr[low]:
        return low
    i=low
    for i in range(high):
        if arr[i]==x:
            return i
        if arr[i]<x and arr[i+1]>=x:
            return i+1
    return -1

arr = [1, 2, 8, 10, 10, 12, 19]
n = len(arr)
x = 3
index = ceilSearch(arr, 0, n-1, x);
 
if index == -1:
    print ("Ceiling of %d doesn't exist in array "% x)
else:
    print ("ceiling of %d is %d"%(x, arr[index]))