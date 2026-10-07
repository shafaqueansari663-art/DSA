# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def flatten(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: None Do not return anything, modify root in-place instead.
        """
        nv=[None]
        def preordeR(root):
            
            if root is None:
                return 
            preordeR(root.right)
            preordeR(root.left)
            root.left=None
            root.right=nv[0]
            nv[0]=root
        preordeR(root)