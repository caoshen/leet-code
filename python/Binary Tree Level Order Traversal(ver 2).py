# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @return a list of lists of integers
    def levelOrder(self, root):
        result = []
        self.traverse( root, 1, result)
        return result
    def traverse(self, root, level, result):
        if root == None:
            return
        if level > len(result):
            result.append([])
        result[level - 1].append(root.val)
        self.traverse(root.left, level + 1, result)
        self.traverse(root.right, level + 1, result)
