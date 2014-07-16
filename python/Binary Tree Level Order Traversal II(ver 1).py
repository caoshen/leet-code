# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @return a list of lists of integers
    def levelOrderBottom(self, root):
        result = []
        self.levelTra(root, 1, result)
        return result[::-1]
    def levelTra(self, root, level, result):
        if root == None:
            return
        if len(result) < level:
            result.append([])
        result[level - 1].append(root.val)
        self.levelTra(root.left, level + 1, result)
        self.levelTra(root.right, level + 1, result)