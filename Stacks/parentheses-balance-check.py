'''

Given a string of opening and closing parentheses, check whether it's
balanced. Three types of parentheses: (), {}, []

'''

def balance_check(s):
    if len(s) %2 == 1:
        return False
    temp = []
    for brac in s:
        if brac in ["(","{","["]:
            temp.append(brac)
        elif brac in ["]","}",")"]:
            if len(temp)==0:
                return False
            elif brac == ")" and temp[-1] == "(":
                temp.pop()
            elif brac == "]" and temp[-1] == "[":
                temp.pop()
            elif brac == "}" and temp[-1] == "{":
                temp.pop()
            else:
                temp.append(brac)
    return len(temp) == 0

def balance_check2(s):
    if len(s) %2 != 0:
        return False
    
    opening = set("([{")
    matches = set([("(",")"),("[","]"),("{","}")])
    stack = []

    for paren in s:
        if paren in opening:
            stack.append(paren)
        else:
            if len(stack) == 0:
                return False
            last_open = stack.pop()
            if (last_open,paren) not in matches:
                return False
    return len(stack) == 0
from nose.tools import assert_equal

class TestBalanceCheck(object):
    
    def test(self,sol):
        assert_equal(sol('[](){([[[]]])}('),False)
        assert_equal(sol('[{{{(())}}}]((()))'),True)
        assert_equal(sol('[[[]])]'),False)
        assert_equal(sol(')[]('),False)
        print('ALL TEST CASES PASSED')
        
# Run Tests

t = TestBalanceCheck()
t.test(balance_check)
t.test(balance_check2)
