'''

Given minimum and maximum values, trim the BST
in such a way that the resulting tree is also a
BST with no values greater than max value and no
values lesser than min value.

'''

def trimBst(tree,minVal,maxVal):
    
    if not tree:
        return
    
    tree.left = trimBst(tree.left,minVal,maxVal)
    tree.right = trimBst(tree.right,minVal,maxVal)
    if minVal <= tree.val <= maxVal:
        return tree
    
    if tree.val < minVal:
        return tree.right
    if tree.val maxVal:
        return tree.left