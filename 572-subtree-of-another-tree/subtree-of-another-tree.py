# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSubtree(self, root, subRoot):
        """
        :type root: Optional[TreeNode]
        :type subRoot: Optional[TreeNode]
        :rtype: bool
        """
        def issame(root,subRoot):
            if root is None or subRoot is None:
                return root==subRoot
            if root.val!=subRoot.val:
                return False
            return issame(root.left,subRoot.left) and issame(root.right,subRoot.right)
        
        if not root:
            return False
        if issame(root,subRoot):
            return True
        return self.isSubtree(root.left,subRoot) or self.isSubtree(root.right,subRoot)
        