'''

Implementation of insertion sort.

'''

def insertion_sort(arr):
	print(arr)
	n = len(arr)
	for i in range(1,n):
		currElement = arr[i]
		position = i
		
		while position>0 and arr[position-1] > currElement:
			arr[position] = arr[position-1]
			position -= 1
		arr[position] = currElement
	print(arr)







from random import randint  

arr = [randint(0,100) for i in range(10)]
insertion_sort(arr)