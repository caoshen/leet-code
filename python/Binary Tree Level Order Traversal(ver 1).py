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
        result , level = [], []
        if root == None:
            return result
        level.append(root)
        result.append(level)
        while True:
            level = []
            for item in result[-1]:
                if item.left != None:
                    level.append(item.left)
                if item.right != None:
                    level.append(item.right)
            if len(level) != 0:
                result.append(level)
            else:
                break
        ans = []
        for level in result:
            al = []
            for node in level:
                al.append(node.val)
            ans.append(al)
        return ans
