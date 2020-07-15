'''

Given an array of elements, count the number of subset pairs,
whose difference is equal to the given value.

For example:
    arr = [1,1,2,3]
    k = 1
    sub-arrays = {[1,2],[1,3]} , {[1,1,2],[3]} , {[1,2],[1,3]} 
    (because there are 2 ones)
    answer = 3

'''

'''

We are given that, s1 - s2 = k
also, s1 + s2 = totalsum
adding these two, we get, 
2*s1 = total + k
s1 = (total + k)//2
so, if we can find s1, there is
definitely an s2 which satisfies
s1 - s2 = k

'''

def countSubsetDiff(arr,k):

    total = sum(arr)
    s1 = (total + k)//2

    dp = [[None] * (s1 + 1) for _ in range(len(arr) + 1)]

    for i in range(len(arr) + 1):
        for j in range(s1 + 1):
            if i == 0:
                dp[i][j] = 0
            if j == 0:
                dp[i][j] = 1
    
    for i in range(1, len(arr) + 1):
        for j in range(1, s1 + 1):
            if j < arr[i-1]:
                dp[i][j] = dp[i-1][j]
            else:
                dp[i][j] = dp[i-1][j-arr[i-1]] + dp[i-1][j]
    
    return dp[len(arr)][s1]

arr = [1,1,2,3]
k = 1
print("The answer for value ",k," is => ",countSubsetDiff(arr,k))
 