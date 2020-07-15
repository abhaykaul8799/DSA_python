'''

Given an array of coins, calculate the number of ways to obtain
a given value.

For example:
    coins = [1,2,3]
    val = 5
    Answer => 5 ({1,1,1,1,1},{1,1,3},{1,1,1,2},{1,2,3},{2,3})

'''

def coinChange(coins,tar):

    dp = [[None] * (tar + 1) for _ in range(len(coins) + 1)]

    for i in range(len(coins)+1):
        for j in range(tar + 1):
            if i == 0:
                dp[i][j] = 0
            if j == 0:
                dp[i][j] = 1
    
    for i in range(1,len(coins) + 1):
        for j in range(1,tar + 1):
            if j < coins[i-1]:
                dp[i][j] = dp[i-1][j]
            else:
                dp[i][j] = dp[i][j-coins[i-1]] + dp[i-1][j]
    
    print("The DP Table is: ")
    print(dp)

    return dp[len(coins)][tar]

coins = [1,2,3]
k = 5
print("For amount = ",k," the number of ways is: ",coinChange(coins,k))