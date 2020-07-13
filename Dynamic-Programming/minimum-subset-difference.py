'''

Given an array of integer elements, form 2 subsets such
that the difference between those two array is minimum.

For example:
    arr = [1,6,11,5]
    subsets = [1,11],[5,6]
    diff = 1 => minimum difference

'''

from numpy import array

def minimumSubsetSum(arr):
    total = sum(arr)
    allSums = subsetSum(arr,total)
    print("The last row of the dp table is: ")
    print(allSums)
    mid = len(allSums)//2
    if mid * 2 == total and allSums[mid]:
        return 0
    else:
        for i in range(mid-1,-1,-1):
            if allSums[i]:
                return total - 2*i


def subsetSum(arr,val):

    dp = [[None] * (val + 1) for _ in range(len(arr) + 1)]

    for i in range(len(arr) + 1):
        for j in range(val+1):
            if i == 0:
                dp[i][j] = False
            if j == 0:
                dp[i][j] = True
    
    for i in range(1,len(arr) + 1):
        for j in range(1,val + 1):
            if j < arr[i-1]:
                dp[i][j] = dp[i-1][j]
            else:
                dp[i][j] = dp[i-1][j-arr[i-1]] or dp[i-1][j]

    return dp[-1]

print()
arr = [1,6,11,5]
print("The answer to array ",arr," is => ",minimumSubsetSum(arr))
print()
arr= [1,2,3,4,5,6,7,8,9,10]
print("The answer to array ",arr," is => ",minimumSubsetSum(arr))
print()
arr = [1,9,2,7,5,6,4,8,3]
print("The answer to array ",arr," is => ",minimumSubsetSum(arr))
print()
arr = [1,3,12,11,8,7,2,9,10,19]
print("The answer to array ",arr," is => ",minimumSubsetSum(arr))
print()
