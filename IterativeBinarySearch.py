def binarySearch(arr, l, r, x):
    
    while l <= r:
        
        #dividing the array in half to find the middle element
        mid = l + (r - l) // 2
        
        #if x is greater then ignore left side
        if arr[mid] == x:
            return mid
        
        #if x is smaller then ignore right side
        elif arr[mid] < x:
            l = mid + 1
            
        #if neither then it means it is the middle element
        else:
            r = mid - 1

    #this means element isn't present
    return -1

#printing the list
arr = [ 10, 30, 40, 2, 5 ]
x = 30
result = binarySearch(arr, 0, len(arr) - 1, x)

if result != -1:
    print("Element is present at index ",str(result))
else:
    print("result no there")
