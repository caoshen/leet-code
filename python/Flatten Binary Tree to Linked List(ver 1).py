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
        stackTree = []
        if root != None:
            stackTree.append(root)
        while len(stackTree) != 0:
            x = stackTree[-1]
            stackTree.pop()
            if x.right != None:
                stackTree.append(x.right)
            if x.left != None:
                stackTree.append(x.left)
            x.left = None
            if len(stackTree) != 0:
                x.right = stackTree[-1]