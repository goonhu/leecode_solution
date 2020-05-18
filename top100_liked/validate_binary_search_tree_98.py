# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# treenode is pre-defined by the question

class Solution:
    def helper(self, node, c_min, c_max):
        if node == None: return True
        if node.val <= c_min or node.val >= c_max:
            return False
        else:
            return self.helper(node.left, c_min, node.val) and self.helper(node.right, node.val, c_max)

    def isValidBST(self, root: TreeNode) -> bool:
        if root == None: return True
        c_max, c_min = float('inf'), -float('inf')
        if root.val <= c_min or root.val >= c_max:
            return False
        else:
            return self.helper(root.left, c_min, root.val) and self.helper(root.right, root.val, c_max)

