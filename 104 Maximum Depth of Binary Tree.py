# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root == None:
            return 0
        else:
            depL = self.maxDepth(root.left)
            depR = self.maxDepth(root.right)
            dep = max(depL,depR)+1
            return dep
    