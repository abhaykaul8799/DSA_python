'''
Given a string of words, reverse the string
Ex-> This is the best => best the is This
Also remove all trailing white spaces

'''

def sent_rev(string):
    return " ".join(string.split()[::-1])

def sent_rev2(string):
    words = []
    length = len(string)
    
    i = 0
    while i<length:
        if string[i] != ' ':
            word_start = i
            while i < length and string[i] != ' ':
                i += 1
            words.append(string[word_start:i])
        i += 1

    return " ".join(reversed(words))


from nose.tools import assert_equal

class ReversalTest(object):
    
    def test(self,sol):
        assert_equal(sol('    space b efore'),'efore b space')
        assert_equal(sol('space after     '),'after space')
        assert_equal(sol('   Hello John    how are you   '),'you are how John Hello')
        assert_equal(sol('1'),'1')
        print("ALL TEST CASES PASSED")
        
# Run and test
t = ReversalTest()
t.test(sent_rev)
t.test(sent_rev2)
