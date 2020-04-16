'''

Representing tree using nodes and references using OOP.
Also the implementation of different types of traversals.

'''

class BinaryTree:

    def __init__(self,rootObj):
        self.key = rootObj
        self.leftChild = None
        self.rightChild = None
    
    def insertLeft(self,newNode):
        if self.leftChild == None:
            self.leftChild = BinaryTree(newNode)
        else:
            l = BinaryTree(newNode)
            l.leftChild = self.leftChild
            self.leftChild = l

    def insertRight(self,newNode):
        if self.rightChild == None:
            self.rightChild = BinaryTree(newNode)
        else:
            r = BinaryTree(newNode)
            r.rightChild = self.rightChild
            self.rightChild = r
    
    def getRightChild(self):
        return self.rightChild
    
    def getLeftChild(self):
        return self.leftChild

    def setRootValue(self,obj):
        self.key = obj
    
    def getRootValue(self):
        return self.key
    

def preorder(root):
    if root:
        print(root.getRootValue(), end=" ")  
        preorder(root.getLeftChild())
        preorder(root.getRightChild())

def inorder(root):
    if root:
        inorder(root.getLeftChild())
        print(root.getRootValue(), end=" ")  
        inorder(root.getRightChild())

def postorder(root):
    if root:
        postorder(root.getLeftChild()) 
        postorder(root.getRightChild())
        print(root.getRootValue(), end=" ") 

    

r = BinaryTree('a')
r.insertLeft('c')
r.insertLeft('b')
r.insertRight('e')
r.insertRight('d')
print("Preorder Traversal:  ", end=" ")
preorder(r)
print()
print("Inorder Traversal:   ", end=" ")
inorder(r)
print()
print("Postorder Traversal: ", end=" ")
postorder(r)

