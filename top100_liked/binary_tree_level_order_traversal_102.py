
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# treenode is pre-defined by the question

class Solution:
    def BFS(self, node):
        answers = []; temp = []
        queue = []
        if node != None:
            queue.append(node); queue.append(None)

        while (len(queue ) !=0):
            current = queue.pop(0)
            if len(queue) == 0: return answers
            if current == None:
                queue.append(None)
                current = queue.pop(0)

            if current.left != None: queue.append(current.left)
            if current.right != None: queue.append(current.right)

            temp.append(current.val)

            if queue[0] == None: answers.append(temp); temp = []

        return answers

    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        answers = self.BFS(root)
        return answers
