'''

Given two arrays, weights and their respective values, and given
a knapsack with weight W, how can we maximise the value of the 
objects inside the knapsack, considering we can take multiple 
occurances of any given item.

'''

def unboundedKnapsack(wt,val,W):

    dp = [[None]*( W + 1) for _ in range(len(wt) + 1)]

    for i in range(len(wt) + 1):
        for j in range(W + 1):
            if i == 0 or j == 0:
                dp[i][j] = 0
    
    for i in range(1,len(wt) + 1):
        for j in range(1,W + 1):
            if j < wt[i-1]:
                dp[i][j] = dp[i-1][j]
            else:
                dp[i][j] = max(val[i-1] + dp[i][j-wt[i-1]],dp[i-1][j])
    
    print("The DP table is: ")
    print(dp)

    return dp[len(wt)][W]

wt = [1,2,3,4,5]
val = [1,2,9,4,5]
W = 10
print("The answer for weights ",wt," and values ",val," and weight ",W," is => ",unboundedKnapsack(wt,val,W))
