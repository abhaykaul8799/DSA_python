'''

Given an array of elements, count the number of subarrays with a given sum.

For example:

'''

def countSubarraySum(arr,k):

    values = dict()
    values[0] = 1
    currsum = 0
    count = 0
    for i in arr:
        currsum += i
        if currsum - k in values:
            count += values[currsum-k]
        if currsum in values:
            values[currsum] += 1
        else:
            values[currsum] = 1
    return count    

arr = [3,4,7,2,-3,1,4,2]
k = 7
print("The answer for value ",k," is => ",countSubarraySum(arr,k))
