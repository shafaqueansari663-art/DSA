# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def sumOfLeftLeaves(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        total=[0]
        def leaf(root):
           
            if not root:
                return 
            if root.left :
                if root.left.right==None and root.left.left == None:
                    total[0]+=root.left.val
            leaf(root.left)
            leaf(root.right)
        leaf(root)
        return total[0]
        
        
        
