# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isValidBST(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """
        def isbst(root,min_val,max_val):
            if root is None:
                return True
            if root.val<=min_val or root.val>=max_val:
                return False
            
            return(isbst(root.left,min_val,root.val)and
            isbst(root.right,root.val,max_val))
        return isbst(root,float('-inf'),float('inf'))
        