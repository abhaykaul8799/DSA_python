'''

Representing trees using List of Lists.

'''

def BinaryTree(r):
    return [r,[],[]]

def insertLeft(root,newBranch):
    t = root.pop(1)
    if len(t)>1:
        root.insert(1,[newBranch,t,[]])
    else:
        root.insert(1,[newBranch,[],[]])
    return root

def insertRight(root,newBranch):
    t = root.pop(2)
    if len(t)>1:
        root.insert(2,[newBranch,[],t])
    else:
        root.insert(2,[newBranch,[],[]])
    return root

def getRootVal(root):
    return root[0]

def setRootValue(root,newVal):
    root[0] = newVal

def getLeftChild(root,newVal):
    return root[1]

def getRightChild(root,newVal):
    return root[2]

r = BinaryTree(3)
print(insertLeft(r,4))
print(insertLeft(r,5))
print(insertRight(r,6))
print(insertRight(r,7))


