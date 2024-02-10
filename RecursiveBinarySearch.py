def binary_search(arr, low, high, x):

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
arr = [ 10, 30, 40, 2, 5 ]
x = 30
result = binary_search(arr, 0, len(arr) - 1, x)

if result != -1:
    print("Element is present at index ",str(result))
else:
    print("result no there")