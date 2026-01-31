# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque 
class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """
        if not root:
            return True
        q1=deque([root.left])
        q2=deque([root.right])

        while q1 and q2:
            n1=q1.popleft()
            n2=q2.popleft()

            if not n1 and not n2 :
                continue
            if not n1 or not n2 :
                return False
            if n1.val!= n2.val:
                return False

            #miroor
            q1.append(n1.left)
            q2.append(n2.right)

            q1.append(n1.right)
            q2.append(n2.left)
        return True
        

        