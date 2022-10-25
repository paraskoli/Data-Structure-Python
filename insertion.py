# Python program for implementation of Insertion Sort

def insertionSort(arr):

	# Traverse through 1 to len(arr)
	for i in range(1, len(arr)):

		key = arr[i]

		# Move elements of arr[0..i-1], that are
		# greater than key, to one position ahead
		# of their current position
		k = i-1
		while k >=0 and key < arr[k] :
				arr[k+1] = arr[k]
				k -= 1
		arr[k+1] = key


#sorting the array [12, 11, 13, 5, 6] using insertionSort
arr = [18,5,6,8,9]
insertionSort(arr)
lst = [] #Empty list
print("Sorted array is : ")
for i in range(len(arr)):
	lst.append(arr[i])	 #appending the elements in sorted order
print(lst)

