# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: Optional[TreeNode]
        :type q: Optional[TreeNode]
        :rtype: bool
        """
        # if both are null it will return true else false
        if p is None or q is None:
            return p==q

        if p.val!=q.val:
            return False


        leftsame=self.isSameTree(p.left,q.left)
        rightsame=self.isSameTree(p.right,q.right)

        return leftsame and rightsame 