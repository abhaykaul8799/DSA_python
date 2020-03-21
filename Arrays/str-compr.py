from collections import Counter

def str_compression(s): # wont work if AABBAACC will give A4B2C2
     if len(s)==0:
        return ''
    if len(s) == 1:
        return s[0]+"1"
    counter = Counter(s)
    items =list(counter.items())
    get = lambda x:x[0]+str(x[1])
    items = list(map(get,items))
    return "".join(items)

def str_compression2(s): # AABBAACC gives A2B2A2C2
    if len(s)==0:
        return ''
    if len(s) == 1:
        return s[0]+"1"
    l = len(s)
    i = 1
    r = ""
    count = 1
    while i<l:
        if s[i] == s[i-1]:
            count += 1
        else:
            r = r + s[i-1] + str(count)
            count = 1
        i+=1
    r = r + s[i-1] + str(count)
    return r

from nose.tools import assert_equal

class TestCompress(object):

    def test(self, sol):
        assert_equal(sol(''), '')
        assert_equal(sol('AABBCC'), 'A2B2C2')
        assert_equal(sol('AAABCCDDDDD'), 'A3B1C2D5')
        assert_equal(sol('AAAaaBBbbCCc'),'A3a2B2b2C2c1')
        print('ALL TEST CASES PASSED')

# Run Tests
t = TestCompress()
t.test(str_compression)
t.test(str_compression2)
