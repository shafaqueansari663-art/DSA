# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def find_min(self,node):
        while node.left:
            node=node.left
        return node

    def deleteNode(self, root, key):
        """
        :type root: Optional[TreeNode]
        :type key: int
        :rtype: Optional[TreeNode]
        """
        if root is None:
            return root 
        elif root.val<key:
            root.right=self.deleteNode(root.right,key)
        elif root.val>key:
            root.left=self.deleteNode(root.left,key)
        else:
            # case1 when leaf node
            if root.left is None and root.right is None:
                return None
            # case 2 when one child 
            elif root.left is None:
                return root.right
            elif root.right is None:
                return root.left
            # case 3 when two child  
            temp=self.find_min(root.right)
            root.val=temp.val
            root.right=self.deleteNode(root.right,temp.val)
        return root

        