# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @return nothing, do it in place
    def flatten(self, root):
        self.dfs(root, None)
    def dfs(self, root, tail):
        if root == None:
            return tail
        root.right = self.dfs(root.left, self.dfs(root.right, tail))
        root.left = None
        return root