def selectionSort(array, size):
	
	for ind in range(size):
		min_index = ind

		for j in range(ind + 1, size):
			
			if array[j] < array[min_index]:
				min_index = j
		
		(array[ind], array[min_index]) = (array[min_index], array[ind])

size = int(input("Enter the size of array: "))
arr = []
for i in range(size):
	arr.append(int(input("Enter the element: ")))
	
selectionSort(arr, size)
print('The array after sorting in Ascending Order by selection sort is:')
print(arr)
