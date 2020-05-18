# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# tree node is pre-defined by the question

class Solution:

    def get_result(self, current, output):

        if current:
            self.get_result(current.left, output)
            output.append(current.val)
            self.get_result(current.right, output)
            return
        else:
            return

    def inorderTraversal(self, root: TreeNode) -> List[int]:
        current = root;
        output = []
        self.get_result(current, output)

        return output
