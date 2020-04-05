'''

Write a function that takes a head node and an integer value
n and then returns the Nth to last node in the linked list.

'''

class Node:

    def __init__(self,value):
        self.value = value
        self.nextnode = None

def nth_to_last_node(n,head):

    counter = 0
    place = head
    while head:
        counter += 1
        head = head.nextnode
    
    head = place

    counter = counter - n
    for i in range(counter):
        head = head.nextnode
    return head

def nth_to_last_node2(n, head):
    slow, fast = head, head
    while n > 0 and fast:
        fast=fast.nextnode
        n-=1
    if not fast:
        return head
    while fast:
        fast=fast.nextnode
        slow=slow.nextnode
    return slow

"""
RUN THIS CELL TO TEST YOUR SOLUTION AGAINST A TEST CASE 
"""

from nose.tools import assert_equal

a = Node(1)
b = Node(2)
c = Node(3)
d = Node(4)
e = Node(5)

a.nextnode = b
b.nextnode = c
c.nextnode = d
d.nextnode = e

####

class TestNLast(object):
    
    def test(self,sol):
        
        assert_equal(sol(2,a),d)
        print ('ALL TEST CASES PASSED')
        
# Run tests
t = TestNLast()
t.test(nth_to_last_node)
t.test(nth_to_last_node2)
