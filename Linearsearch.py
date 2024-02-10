def Linear(arr, N, x):
    for i in range(0, N):
        if arr[i] == x:
            return i
    return -1

arr = [10,50,30,40,20]
x = 40
N = len(arr)
result = Linear(arr, N, x)
if result != -1:
    print("Element is present at index : ",result )
else:
    print("element no there")
