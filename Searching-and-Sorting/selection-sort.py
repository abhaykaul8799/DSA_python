'''

Implementation of Selection sort.

'''

def selection_sort(arr):

    n = len(arr)
    print(arr)
    for i in range(n):
        min_num = arr[i]
        index = i
        for j in range(i+1,n):
            if arr[j] < min_num:
                index =  j
                min_num = arr[j]
        if arr[i] > min_num:
            arr[i], arr[index] = arr[index] , arr[i]
    print(arr)
    print(arr == sorted(arr))

from random import randint  

arr = [randint(0,100) for i in range(10)]
selection_sort(arr)