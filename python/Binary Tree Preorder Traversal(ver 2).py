# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @return a list of integers
    def preorderTraversal(self, root):
        stackT , result = [], []
        if root != None:
            stackT.append(root)
        while len(stackT) > 0:
            x = stackT[-1]
            result.append(x.val)
            stackT.pop()
            if x.right != None:
                stackT.append(x.right)
            if x.left != None:
                stackT.append(x.left)
        return result