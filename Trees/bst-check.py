'''

Check if the given tree is a BST or not.

'''


class Tree:
    def __init__(self,value):
        self.value = value
        self.left = None
        self.right = None

### Solution 1
tree_vals = []

def inorder(tree):
    if tree:
        inorder(tree.left)
        tree_vals.append(tree.value)
        inorder(tree.right)

def check(tree_vals):
    return tree_vals == sorted(tree_vals)

tree = Tree(10)
tree.left = Tree(5)
tree.right = Tree(10)

inorder(tree)
print(check(tree_vals))

### Solution 2

def tree_max(node):
    if not node:
        return float("-inf")
    rightmax = tree_max(node.right)
    leftmax = tree_max(node.left)
    return max(node.value,rightmax,leftmax)

def tree_min(node):
    if not node:
        return float("inf")
    leftmin = tree_min(node.left)
    rightmin = tree_min(node.right)
    return min(node.value,leftmin,rightmin)

def verify(node):
    if not node:
        return True
    if (tree_max(node.left)<=node.value <= tree_min(node.right) and verify(node.left) and verify(node.right)):
        return True
    else:
        return False

t = Tree(10)
t.left = Tree(5)
t.right = Tree(20)

print(verify(t))