'''

Given an array of items with different weights, another array with their respective values,
and a target weight, fill the weight such that the total value is maximized.
(A weight can only be taken once.)

For example:
    wt     = [1,2,3,4,5]
    val    = [1,3,4,3,2]
    target = 8
    ansval = [1,3,4] (weights) => 1 + 4 + 3 => 8 (sum of value)
    target = 6
    ansval = [1,2,3] (weights) => 1 + 3 + 4 => 8 (sum of values)

'''

from numpy import array

def knapsack(wt,val,tar):
    '''
    wt  : <int> array with weight of elements
    val : <int> array with value of elements
    tar : <int> target weight
    returns => <int> Maximum value possible
    '''

    dp = [[None] * (target + 1) for _ in range(len(wt) + 1)]

    for i in range(len(wt) + 1):
        for j in range(target+1):
            if i == 0 or j == 0:
                dp[i][j] = 0
    
    for i in range(1,len(wt)+1):
        for j in range(1,target+1):
            if j<wt[i-1]:
                # if current weight is bigger than target, check for the max value for previous weights and put that
                dp[i][j] = dp[i-1][j]
            else:
                # check which value is bigger, taking the current weight, or leaving the current weight
                # if we take the current weight, check the value of max value for target = target - currweight
                # and excluding the current weight. For example, if we take 3, froman array of [1,3,5] for target
                # 6, new target is 3 and we will check with weight 1.
                dp[i][j] = max(dp[i-1][j],val[i-1]+dp[i-1][j-wt[i-1]])
    
    print("The dp array is: ")
    print(array(dp))

    return dp[len(wt)][target]

wt = [1,2,3,4,5]
val = [1,3,4,3,2]
target = 8

print("Answer = ",knapsack(wt,val,target))

    
