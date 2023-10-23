
def binary_search(arr, low, high, x):

	if high >= low:

		mid = (high + low) // 2

		if arr[mid] == x:
			return mid

		elif arr[mid] > x:
			return binary_search(arr, low, mid - 1, x)

		else:
			return binary_search(arr, mid + 1, high, x)

	else:
		return -1

size = int(input("Enter the size of array: "))
arr = []
for i in range(size):
	arr.append(int(input("Enter the element: ")))

key = int(input("Enter the key element to find: "))

result = binary_search(arr, 0, len(arr)-1, key)

if result != -1:
	print("Element is present at index", str(result))
else:
	print("Element is not present in array")
