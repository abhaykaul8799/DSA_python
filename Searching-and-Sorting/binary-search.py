'''

Implementation of binary search in python.

'''

from random import randint

arr = []

for i in range(1000):
    arr.append(randint(1,1001))

arr = list(set(arr))
arr.sort()

x = randint(1,1000)

### Iterative version:

def binary_search(arr,element):

    first = 0
    last = len(arr) - 1
    found = False

    while first <= last and not found:
        mid = (first+last)//2

        if arr[mid] == element:
            found = True
        else:
            if element < arr[mid]:
                last = mid -1
            else:
                first = mid + 1
    return found

### Recursive version:

def rec_binary_search(arr,ele):

    first = 0
    last = len(arr) - 1
    mid = last//2
    
    if len(arr) == 0:
        return False
    
    elif arr[mid] == ele:
        return True
    else:
        if arr[mid] < ele:
            return rec_binary_search(arr[mid+1:],ele)
        else:
            return rec_binary_search(arr[:mid],ele)

print("The Number is: ",x)
print(binary_search(arr,x))
print(rec_binary_search(arr,x))
