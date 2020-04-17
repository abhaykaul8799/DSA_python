'''

Print the tree in level order.

'''


class Node:
    def __init__(self,value):
        self.value = value
        self.left = None
        self.right = None

### Solution 1

ordered = []
def level(node,lvl=0):
    if node:
        ordered.append((lvl,node.value))
        lvl += 1
        level(node.left,lvl)
        level(node.right,lvl)

t = Node(1)
t.left = Node(2)
t.right = Node(3)
t.left.left = Node(4)
t.left.right = Node(5)
t.right.left = Node(6)
t.right.right = Node(7)

level(t)
ordered.sort(key = lambda x:x[0])

print(ordered)

prev = 0
for lvl,value in ordered:
    if lvl == prev:
        print(value,end=" ")
    else:
        print(f"\n{value}",end = " ")
    prev = lvl
print()
print("-"*20)
### Solution 2


def levelOrderPrint(tree):
    if not tree:
        return
    
    nodes =[tree]
    currCount = 1
    nextCount = 0
    while len(nodes) != 0:
        currentNode = nodes.pop(0)
        currCount -= 1
        print(currentNode.value, end=" ")
        if currentNode.left:
            nodes.append(currentNode.left)
            nextCount += 1
        if currentNode.right:
            nodes.append(currentNode.right)
            nextCount += 1
        
        if currCount == 0:
            print()
            currCount, nextCount = nextCount, currCount
levelOrderPrint(t)

