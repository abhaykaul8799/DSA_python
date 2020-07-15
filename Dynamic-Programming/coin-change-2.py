'''

Given an array of coins, figure out the minimum number of coins
required to make the target value.

For example:
    coins = [1,2,3]
    tar = 5
    Answer => 2 ({2,3})

'''

def coinChange2(coins,tar):

    dp = [[None] * (tar + 1) for _ in range(len(coins) + 1)]
    
    ###
    # If we have 0 coins, it will take infinite number 
    # of coins to get to the value.
    # If we have to get to value 0, we require 0 coins.
    ###
    for i in range(len(coins) + 1):
        for j in range(tar + 1):
            if i==0:
                dp[i][j] = float("inf")
            if j == 0 and i != 0:
                dp[i][j] = 0
    
    ###
    # Unique initialization for this type of problem.
    # We initialize the second row also.
    ###

    for i in range(1,tar+1):
        if i % coins[0] == 0:
            dp[1][i] = i//coins[0]
        else:
            dp[1][i] = float("inf")

    
    for i in range(2,len(coins) + 1):
        for j in range(1,tar + 1):
            if j < coins[i-1]:
                dp[i][j] = dp[i-1][j]
            else:
                dp[i][j] = min(1 + dp[i][j-coins[i-1]],dp[i-1][j])
    
    print("The DP table is: ")
    print(dp)

    return dp[len(coins)][tar]

coins = [2,3,1]
k = 5

print("The answer to amount = ",k," is => ",coinChange2(coins,k)," coins.")
