'''

Given an array of elements, check whether it is possible to 
form the target number using + or - operations.

For example:
    arr = [1,1,2,3]
    tar = 1
    Answer => True (1-1-2+3)

'''

def targetSum(arr,val):
    total = sum(arr)
    tar = (total + val)//2
    
    dp = [[None] * (tar + 1) for _ in range(len(arr) + 1)]

    for i in range(len(arr) + 1):
        for j in range(tar + 1):
            if i == 0:
                dp[i][j] = False
            if j == 0:
                dp[i][j] = True
    
    for i in range(1,len(arr) + 1):
        for j in range(1,tar + 1):
            if j < arr[i-1]:
                dp[i][j] = dp[i-1][j]
            else:
                dp[i][j] = dp[i-1][j] or dp[i-1][j-arr[i-1]]
    
    return dp[len(arr)][tar]

arr = [1,1,2,3]
k = 4
print("Answer for target value ",k," is => ",targetSum(arr,k))
