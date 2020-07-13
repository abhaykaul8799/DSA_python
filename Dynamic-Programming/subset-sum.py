'''

Given an array of values and a target sum, check wether the given sum is possible 
to be made from the subset of the given elements.

For example:
    arr = [1,3,5]
    tar = 4
    ANSWER => True
    tar = 2
    ANSWER => False

'''

from numpy import array

def subsetsum(arr,val):
    '''
    arr : <int> array
    val : <int> target value
    RETURNS => <bool> if it is possible or not
    '''

    dp = [[None] * (val + 1) for _ in range(len(arr) + 1)]

    for i in range(len(arr) + 1):
        for j in range(val + 1):
            if i == 0:
                dp[i][j] = False
            if j == 0:
                dp[i][j] = True
    
    for i in range(1,len(arr)+1):
        for j in range(1,val+1):
            if j < arr[i-1]:
                dp[i][j] = dp[i-1][j]
            else:
                dp[i][j] = dp[i-1][j] or dp[i-1][j-arr[i-1]]
    
    print("The dp array is: ")
    print(array(dp))

    return dp[len(arr)][val]

arr = [1,3,5]
print()
print("For target = 0, answer is =>",subsetsum(arr,0))
print()
print("For target = 2, answer is =>",subsetsum(arr,2))
print()
print("For target = 4, answer is =>",subsetsum(arr,4))
print()