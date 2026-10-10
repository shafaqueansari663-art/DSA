# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def kthSmallest(self, root, k):
        """
        :type root: Optional[TreeNode]
        :type k: int
        :rtype: int
        """
        count=[0]
        result=[None]
        def inorder(root):
            if root is None:
                return 
            
            inorder(root.left)

            count[0]+=1
            if count[0]==k:
                result[0]=root.val
                return
            inorder(root.right)
        inorder(root)
        return result[0]

        