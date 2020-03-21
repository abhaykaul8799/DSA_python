from collections import defaultdict

def unq(s):
    d = defaultdict(int)
    for i in s:
        if d[i]>0:
            return False
        d[i] = 1
    return True

def unq2(s):
    return len(s) == len(set(s))

def unq3(s):
    seen = set()

    for i in s:
        if i not in seen:
            seen.add(i)
        else:
            return False
    return True

from nose.tools import assert_equal


class TestUnique(object):

    def test(self, sol):
        assert_equal(sol(''), True)
        assert_equal(sol('goo'), False)
        assert_equal(sol('abcdefg'), True)
        print('ALL TEST CASES PASSED')
        
# Run Tests
t = TestUnique()
t.test(unq)
t.test(unq2)
t.test(unq3)

