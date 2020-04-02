'''

Given a singly linked list,write a function which takes in the first
node in a singly linked list and returns a boolean indicating if the
linked list contains a cycle.

'''

class Node:
    def __init__(self,value):
        self.value = value
        self.nextnode = None

def check_cycle(node):
    header = node
    seen = set()
    seen.add(header)
    if header.nextnode == None:
        # print("out")
        return False
    header = header.nextnode
    while header.nextnode != None:
        # print("in")
        if header not in seen:
            seen.add(header)
            # print(seen)
            header = header.nextnode
        else:
            return True
    # print(seen)
    return False

def cycle_check(node):
#     Use fast and slow pointer
    fast, slow = node, node
    # print(fast.nextnode)
    while fast and fast.nextnode:
        fast = fast.nextnode
        if fast == slow:
            return True
        fast = fast.nextnode
        slow = slow.nextnode
    return False

from nose.tools import assert_equal

# CREATE CYCLE LIST
a = Node(1)
b = Node(2)
c = Node(3)

a.nextnode = b
b.nextnode = c
c.nextnode = a # Cycle Here!


# CREATE NON CYCLE LIST
x = Node(1)
y = Node(2)
z = Node(3)

x.nextnode = y
y.nextnode = z


#############
class TestCycleCheck(object):
    
    def test(self,sol):
        assert_equal(sol(a),True)
        assert_equal(sol(x),False)
        
        print ("ALL TEST CASES PASSED")
        
# Run Tests

t = TestCycleCheck()
t.test(check_cycle)
t.test(cycle_check)