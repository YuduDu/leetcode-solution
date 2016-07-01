# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        self.result = []
        
        def getlevelorder(l,node):
            if node:
                if len(self.result)<l+1:
                    self.result.append([node.val])
                else:
                    self.result[l].append(node.val)
                self.result
                getlevelorder(l+1,node.left)
                getlevelorder(l+1,node.right)
                return self.result
            else:
                return None
                
                
        getlevelorder(0,root)
        return self.result