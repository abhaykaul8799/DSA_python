'''

Implementation of Bubble Sort.

'''

def bubble_sort(arr):

    n = len(arr)
    print(arr)
    for i in range(n):
        for j in range(n-i-1):
            if arr[j]>arr[j+1]:
                arr[j], arr[j+1] = arr[j+1],arr[j]
    print(arr)

from random import randint  

arr = [randint(0,100) for i in range(10)]
bubble_sort(arr)