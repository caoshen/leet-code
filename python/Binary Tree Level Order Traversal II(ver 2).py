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
        result, level = [], []
        if root == None:
            return []
        level.append(root)
        result.append(level)
        while len(level) != 0:
            level = []
            for x in result[0]:
                if x.left != None:
                    level.append(x.left)
                if x.right != None:
                    level.append(x.right)
            if len(level) > 0:
                result.insert(0, level)
        ans = []
        for i in result:
            al = []
            for j in i:
                al.append(j.val)
            ans.append(al)
        return ans
            