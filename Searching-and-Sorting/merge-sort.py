'''

Implementation of Merge Sort in python.

'''

def merge_sort(arr):
    if len(arr)>1:

        mid = len(arr)//2
        lefthalf = arr[:mid]
        righthalf = arr[mid:]
        
        merge_sort(lefthalf)
        merge_sort(righthalf)

        i,j,k = 0,0,0

        while i<len(lefthalf) and j<len(righthalf):
            if lefthalf[i] < righthalf[j]:
                arr[k] = lefthalf[i]
                i += 1
            else:
                arr[k] = righthalf[j]
                j += 1
            
            k += 1
        while i<len(lefthalf):
            arr[k] = lefthalf[i]
            k += 1
            i += 1
        while j<len(righthalf):
            arr[k] = righthalf[j]
            j += 1
            k += 1
    print(arr)

from random import randint  

arr = [randint(0,100) for i in range(10)]
print(arr)
merge_sort(arr)