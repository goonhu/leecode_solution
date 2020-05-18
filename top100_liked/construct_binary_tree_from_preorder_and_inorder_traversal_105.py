
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# treenode is pre-defined by the question

class Solution:

    #     def helper(self, pre, inorder):

    #         first_ele = pre[0]
    #         index = inorder_list.index(first_ele)
    #         left = inorder_list[:index]; right = inorder_list[index:]
    #         return index, inorder_list[index]


    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        if inorder:
            index = inorder.index(preorder.pop(0))
            root = TreeNode(inorder[index])
            root.left = self.buildTree(preorder, inorder[:index])
            root.right = self.buildTree(preorder, inorder[index +1:])

            return root



        # tree = TreeNode(preorder[0])
        # index, val = self.helper(preorder, inorder)
        # tree.left = TreeNode(val)
        # left_pre = preorder[1:]
        # left_inorder = inorder[:index]
        # right_pre = preorder[1:]
        # right_inorder = inorder[index:]
