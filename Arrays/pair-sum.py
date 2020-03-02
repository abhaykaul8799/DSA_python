'''
Given an integer array, output all the unique pairs that sum up to 
a specific value k
'''

def pair_sum(arr,k):

    if len(arr) < 2:
        return 0
    
    seen = set()
    output = set()

    for num in arr:
        target = k - num

        if target not in seen:
            seen.add(num)
        else:
            output.add((min(target,num),max(target,num)))
    return len(output)

from nose.tools import assert_equal

class TestPair():
    
    def test(self,sol):
        assert_equal(sol([1,9,2,8,3,7,4,6,5,5,13,14,11,13,-1],10),6)
        assert_equal(sol([1,2,3,1],3),1)
        assert_equal(sol([1,3,2,2],4),2)
        print('ALL TEST CASES PASSED')
        
#Run tests
t = TestPair()
t.test(pair_sum)