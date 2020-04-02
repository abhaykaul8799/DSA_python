'''

Implementation of singly linked list.

'''

class Node:

    def __init__(self,value):
        self.value = value
        self.nextNode = None

a = Node(1)
b = Node(2)
c = Node(3)

a.nextNode = b
b.nextNode = c

print(a.nextNode.value)

# Circular Linked List
ac = Node(1)
bc = Node(2)
cc = Node(3)
ac.nextNode = bc
bc.nextNode = cc
cc.nextNode = ac
temp = ac

for i in range(10):
    print(temp.value, end = "   ")
    temp = temp.nextNode