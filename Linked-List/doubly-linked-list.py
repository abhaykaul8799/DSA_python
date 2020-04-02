'''

Implementation of doubly linked list.

'''

class Node:

    def __init__(self,value):
        self.value = value
        self.nextNode = None
        self.prevNode = None

header = Node(None)
a = Node(1)
b = Node(2)
c = Node(3)
trailer = Node(None)

header.nextNode = a
a.prevNode = header
a.nextNode = b
b.prevNode = a
b.nextNode = c
c.prevNode = b
c.nextNode = trailer
trailer.prevNode = c

print(a.nextNode.value)
print(b.prevNode.value)

# Circular Doubly Linked List

ac = Node(1)
bc = Node(2)
cc = Node(3)
ac.nextNode = bc
bc.nextNode = cc
cc.nextNode = ac
ac.prevNode = cc
cc.prevNode = bc
bc.prevNode = ac
temp = ac

for i in range(9):
    print(temp.value, end = "   ")
    temp = temp.nextNode

temp = ac
print()
for i in range(9):
    print(temp.value, end = "   ")
    temp = temp.prevNode