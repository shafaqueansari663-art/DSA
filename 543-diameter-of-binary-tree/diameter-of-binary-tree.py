# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def diameterOfBinaryTree(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        #global variableto storre max dia 
        self.ans=0
        def height(root):
            if not root:
                return 0
            left_height=height(root.left)
            right_height=height(root.right)
            self.ans=max(left_height+right_height,self.ans)

            return 1+max(left_height,right_height)
            
        height(root)
        return self.ans