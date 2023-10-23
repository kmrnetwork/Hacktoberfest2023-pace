def insertionSort(arr):
	n = len(arr) 
	
	if n <= 1:
		return 
	for i in range(1, n): 
		key = arr[i] 
		j = i-1
		while j >= 0 and key < arr[j]: 
			arr[j+1] = arr[j] 
			j -= 1
		arr[j+1] = key


size = int(input("Enter the size of array: "))
arr = []
for i in range(size):
	arr.append(int(input("Enter the element: ")))
	
insertionSort(arr)
print(arr)
