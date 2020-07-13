'''

Given an array, check if it can be split into two sub-arrays with
equal sum.

For example:
    arr = [1,2,3,4]
    sub-arrays = [1,4] , [2,3]
    ANSWER => True

'''

from numpy import array

def equalSumPartition(arr):
    '''
    arr : <int> array with different values
    RETURNS => <bool> whether it is possible or not
    '''

    # s1 = sum of subarray 1, s2 = sum of subarray 2
    # s1 = s2 and also s1 + s2 = total sum of the array
    # so, by this, we can infer that 2*s1 = total sum
    # s1 = total sum / 2
    # so, it is never possible if total sum is odd
    # and we just need to find total sum / 2 to get 2 sub arrays of equal sum

    if sum(arr) % 2 == 1:
        return False
    
    val = sum(arr) // 2

    dp = [[None] * (val + 1) for _ in range(len(arr) + 1)]

    for i in range(len(arr) + 1):
        for j in range(val + 1):
            if i == 0:
                dp[i][j] = False
            if j == 0:
                dp[i][j] = True
    
    for i in range(1,len(arr) + 1):
        for j in range(1,val+1):
            if j < arr[i-1]:
                dp[i][j] = dp[i-1][j]
            else:
                dp[i][j] = dp[i-1][j] or dp[i-1][j-arr[i-1]]
    
    print("The dp array is: ")
    print(array(dp))

    return dp[len(arr)][val]

arr = [1,2,3,4]
print("Answer of array = ",arr," is => ",equalSumPartition(arr))
print()
arr = [1,2,3,6]
print("Answer of array = ",arr," is => ",equalSumPartition(arr))
print()
arr = [1,2,3,10]
print("Answer of array = ",arr," is => ",equalSumPartition(arr))
print()
arr = [0]
print("Answer of array = ",arr," is => ",equalSumPartition(arr))
print()
arr = [1,2,3]
print("Answer of array = ",arr," is => ",equalSumPartition(arr))
print()
arr = [2,3]
print("Answer of array = ",arr," is => ",equalSumPartition(arr))
print()