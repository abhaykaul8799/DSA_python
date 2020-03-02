'''

To create a program to check whether two words/sentences are
anagrams of each other or not.

'''

def anagram_check(s1,s2):

    s1 = "".join(s1.lower().split())
    s2 = "".join(s2.lower().split())
    if len(s1) != len(s2):
        return False
    d1 = {}
    d2 = {}

    for i in s1:
        try:
            d1[i] += 1
        except:
            d1[i] = 1
    
    for i in s2:
        try:
            d2[i] += 1
        except:
            d2[i] = 1
    
    if d1==d2:
        return True
    else:
        return False

def anagram_check2(s1,s2):
    s1 = s1.replace(" ","").lower()
    s2 = s2.replace(" ","").lower()
    return sorted(s1) == sorted(s2)


from nose.tools import assert_equal

class AnagramTest(object):
    
    def test(self,sol):
        assert_equal(sol('go go go','gggooo'),True)
        assert_equal(sol('abc','cba'),True)
        assert_equal(sol('hi man','hi     man'),True)
        assert_equal(sol('aabbcc','aabbc'),False)
        assert_equal(sol('123','1 2'),False)
        print('ALL TEST CASES PASSED')

# Run Tests
t = AnagramTest()
t.test(anagram_check)
t.test(anagram_check2)
print(anagram_check("clint eastwood,"))