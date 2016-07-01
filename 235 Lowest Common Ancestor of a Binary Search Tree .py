# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        
        def subnode(root, node):
            if root == None:
                return False
            elif root.val == node.val:
                return True
            else:
                return subnode(root.left,node) or subnode(root.right, node)
        
        if root ==None:
            return None
        elif root.val == p.val or root.val ==q.val:
            return root
        else:
            lp=subnode(root.left,p) 
            rq = subnode(root.right,q)
            lq = subnode(root.left,q)
            rp = subnode(root.right,p)
            if lp and rq:
                return root
            elif lq and rp:
                return root
            elif lq and lp:
                return self.lowestCommonAncestor(root.left,p,q)
            elif rq and rp:
                return self.lowestCommonAncestor(root.right,p,q)
            else:
                return None