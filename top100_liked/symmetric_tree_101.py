# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# treenode is pre-defined by the question

class Solution:
    def helper(self, L, R):

        if L == None and R == None:
            return True
        elif L != None and R != None:
            if L.val != R.val:
                return False
            else:
                return self.helper(L.left, R.right) and self.helper(L.right, R.left)
        return False

    def isSymmetric(self, root: TreeNode) -> bool:
        if root is None:
            return True
        else:
            return self.helper(root.left, root.right)

