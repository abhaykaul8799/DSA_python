'''

Implementation of Shell Sort in python.

'''

def shell_sort(arr):
    print(arr)
    sublistcount = len(arr)//2
    while sublistcount > 0:
        for start in range(sublistcount):
            gap_insertion_sort(arr,start,sublistcount)
        sublistcount = sublistcount//2
    print(arr)

def gap_insertion_sort(arr,start,gap):
    for i in range(start+gap,len(arr),gap):
        currentValue = arr[i]
        position = i
        while position >= gap and arr[position-gap] > currentValue:
            arr[position] = arr[position-gap]
            position -= gap
        arr[position] = currentValue

from random import randint  

arr = [randint(0,100) for i in range(10)]
shell_sort(arr)