'''
Given an array of integers (positive or negative), find the largest
continuous sum.

'''

def max_cont_sum(arr):
    if len(arr) == 0:
        return 0
    if len(arr) == 1:
        return arr[0]
    
    curr_sum = max_sum = arr[0]

    for num in arr[1:]:
        curr_sum = max(curr_sum+num,num)
        max_sum = max(max_sum,curr_sum)
    return max_sum

from nose.tools import assert_equal

class LargeContTest(object):
    def test(self,sol):
        assert_equal(sol([1,2,-1,3,4,-1]),9)
        assert_equal(sol([1,2,-1,3,4,10,10,-10,-1]),29)
        assert_equal(sol([-1,1]),1)
        print('ALL TEST CASES PASSED')
        
#Run Test
t = LargeContTest()
t.test(max_cont_sum)
