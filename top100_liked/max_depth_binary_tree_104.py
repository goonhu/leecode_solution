
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# treenode is pre-defined by the question

class Solution:
    def helper(self, root, c_length):
        queue = []; lengths = []
        queue.append((root, c_length))

        while(len(queue ) >0):
            current = queue.pop(0)
            if current[0] == None: continue
            lengths.append(current[1])
            if current[0] != None:
                queue.append((current[0].left, current[1 ] +1))
                queue.append((current[0].right, current[1 ] +1))

        return lengths

    def maxDepth(self, root: TreeNode) -> int:
        if root == None: return 0
        c_length = 1; len_list = self.helper(root, c_length)
        return max(len_list)
