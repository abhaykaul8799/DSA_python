'''

Given a target amount n and a list (array) of distinct coin values,
what's the fewest coins needed to make the change amount.

For Example:

If n = 10 and coins = [1,5,10] . Then there are 4 possible ways to 
make change:
1*10
5*1 + 1*5
5*2
10*1
with 1 coin being the minimum amount

'''

# Non Recursive Manner (Not Suitable) Greedy Approach
### For cases like (6,[1,3,4]) it will take 4,1,1 as
### answer and return 3 but actual solution is 3,3 and
### the answer 2.
def coin(n,coins):
    count = 0
    for i in coins[::-1]:
        times = n//i
        if times >0:
            count += times
            n = n - i*times
        if n == 0:
            break
    return count

# Recursive without DP
### Still will give wrong answers in some cases
def rec_coin(n,coins):
    
    min_coins = target

    if target in coins:
        return 1

    else:
        for i in [c for c in coins if c<=target]:
            num_coins = 1 + rec_coin(target - i,coins)
            if num_coins<min_coins:
                min_coins = num_coins
    return min_coins

# Recursive with DP
def rec_dp_coin(target,coins,known_results=[0]*1000):

    min_coins = target

    if target in coins:
        known_results[target] = 1
        return 1
    
    elif known_results[target]>0:
        return known_results[target]
    
    else:
        for i in [c for c in coins if c <= target]:
            num_coins = 1 + rec_dp_coin(target-i,coins,known_results)

            if num_coins < min_coins:
                min_coins = num_coins
                known_results[target] = min_coins

    return min_coins





from nose.tools import assert_equal

class TestCoins(object):
    
    def check(self,solution):
        coins = [1,5,10,25]
        assert_equal(solution(45,coins),3)
        assert_equal(solution(23,coins),5)
        assert_equal(solution(74,coins),8)
        assert_equal(solution(6,[1,3,4]),2) 
        print ('Passed all tests.')
# Run Test

test = TestCoins()
# test.check(coin)
test.check(rec_dp_coin)
