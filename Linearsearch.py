def Linear(arr, N, x):
    
    #Iterate through the entire array
    for i in range(0, N):
        
        #check if current element is equal to the key element
        if arr[i] == x:
            
            #Return the index if element is found
            return i
        
    #If element is not found then return -1    
    return -1

#Print the list
arr = [10,50,30,40,20]
x = 40
N = len(arr)
result = Linear(arr, N, x)
if result != -1:
    print("Element is present at index : ",result )
else:
    print("element no there")
