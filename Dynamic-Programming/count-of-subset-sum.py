'''

Given an array of elements, count the number of subarrays, that can be made
which, when added, get to a target value.

For Example:
    arr = [1,2,3]
    tar = 3
    sub-arrays = [1,1,1], [1,2], [3]
    ans = 3

'''

from numpy import array

def countSubset(arr: [int],val: int) -> int:
    '''
    arr : <int> Array of integer numbers
    val : <int> target value
    RETURNS => <int> count of subsets with sum equal to that value
    '''

    dp = [[None] * (val + 1) for _ in range(len(arr) + 1)]

    for i in range(len(arr) + 1):
        for j in range(val + 1):
            if i == 0:
                dp[i][j] = 0
            if j == 0:
                dp[i][j] = 1

    for i in range(1,len(arr) + 1):
        for j in range(1,val + 1):
            if j < arr[i-1]:
                dp[i][j] = dp[i-1][j]
            else:
                dp[i][j] = dp[i-1][j-arr[i-1]] + dp[i-1][j]
    
    print("The dp table is: ")
    print(array(dp))
    
    return dp[len(arr)][val]

arr = [1,2,3,4,5,6,7,8,9,10]
tar = 8
print("Answer with target = ",tar," is => ",countSubset(arr,tar))
tar = 2
print("Answer with target = ",tar," is => ",countSubset(arr,tar))