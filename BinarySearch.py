def binary_search(arr, x):
	low = 0
 
    #finding the index of the last element
	high = len(arr) - 1

	while low <= high:
     
        #dividing the array in half to find the middle element
		mid = (high + low) // 2

		#if x is greater then ignore left side
		if arr[mid] < x:
			low = mid + 1

		#if x is smaller then ignore right side
		elif arr[mid] > x:
			high = mid - 1

		#if neither then it means it is the middle element
		else:
			return mid

	#this means element isn't present
	return -1


#printing the list
arr = [ 2, 3, 4, 10, 40 ]
x = 10
result = binary_search(arr, x)
print("Element is present at index ",str(result))