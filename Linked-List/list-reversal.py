'''

Write a function to reverse a Linked List in place.
The function will take in the head of the list as 
input and return the new head of the list.

'''

class Node:

    def __init__(self,value):
        self.value = value
        self.nextnode = None

# Not Inplace
def reverse(head):
    placeholder = head
    temp = list()
    while head.nextnode != None:
        temp.append(head.value)
        head = head.nextnode
    temp.append(head.value)
    temp = temp[::-1]
    head = placeholder
    for value in temp:
        head.value = value
        head = head.nextnode
    return placeholder

# Inplace
def reverse2(head):
    cur = head
    pre, nxt = None, None
    while cur:# watch out
        nxt = cur.nextnode
        cur.nextnode = pre
        pre = cur
        cur = nxt
    return pre #watch out
    pass


# Create a list of 4 nodes
a = Node(1)
b = Node(2)
c = Node(3)
d = Node(4)

# Set up order a,b,c,d with values 1,2,3,4
a.nextnode = b
b.nextnode = c
c.nextnode = d

print(a.value)
print(a.nextnode.value)
print(b.nextnode.value)
print(c.nextnode.value)

reverse(a)

print(a.value)
print(a.nextnode.value)
print(b.nextnode.value)
print(c.nextnode.value)

print("*"*10)
# Create a list of 4 nodes
a = Node(1)
b = Node(2)
c = Node(3)
d = Node(4)

# Set up order a,b,c,d with values 1,2,3,4
a.nextnode = b
b.nextnode = c
c.nextnode = d
print(a.value)
print(a.nextnode.value)
print(b.nextnode.value)
print(c.nextnode.value)

reverse2(a)

print(d.value)
print(d.nextnode.value)
print(c.nextnode.value)
print(b.nextnode.value)