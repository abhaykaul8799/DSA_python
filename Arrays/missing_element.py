'''

Consider an array of non-negative integers. A second array is formed by shuffling the elements of the first
array and deleting a random element. Given these two arrays, find which element is missing in the second array 

'''


# O(N log N)
def finder(arr1,arr2):
    arr1.sort()
    arr2.sort()

    for i,j in zip(arr1,arr2):
        if i != j:
            return i
    return arr1[-1]

# O(N)

from collections import defaultdict

def finder2(arr1,arr2):
    dfd = defaultdict(int)
    for num in arr2:
        dfd[num] += 1
    for num in arr1:
        if dfd[num] == 0:
            return num
        else:
            dfd[num] -= 1

# O(N) and constant space complexity

def finder3(arr1,arr2):
    result = 0
    for num in arr1+arr2:
        result ^= num
    return result

# O(N) but overflow problem with large numbers, lots of numbers and loss of 
# information problem for floating point numbers

def finder4(arr1,arr2):
    return sum(arr1) - sum(arr2)

# Test Cases

from nose.tools import assert_equal

class TestFinder(object):
    
    def test(self,sol):
        assert_equal(sol([5,5,7,7],[5,7,7]),5)
        assert_equal(sol([1,2,3,4,5,6,7],[3,7,2,1,4,6]),5)
        assert_equal(sol([9,8,7,6,5,4,3,2,1],[9,8,7,5,4,3,2,1]),6)
        print('ALL TEST CASES PASSED')

# Run test
t = TestFinder()
t.test(finder)
t.test(finder2)
t.test(finder3)
t.test(finder4)
