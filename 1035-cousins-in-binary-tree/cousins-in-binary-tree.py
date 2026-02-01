# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution(object):
    def isCousins(self, root, x, y):
        """
        :type root: Optional[TreeNode]
        :type x: int
        :type y: int
        :rtype: bool
        """
        # queue stores node, parent 
        queue=deque([(root,None)])
        while queue:
            size=len(queue)
            x_parent=None
            y_parent=None
            for _ in range(size):
                node,parent=queue.popleft()
                #finding x cousin parent
                if node.val==x:
                    x_parent=parent
                #finding right cousin parent
                if node.val==y:
                    y_parent=parent
    
                if node.left :
                    queue.append([node.left,node])
                if node.right:
                    queue.append([node.right,node])
            #checking is both parents are diffr or not        
            if x_parent and y_parent:
                return x_parent!=y_parent
            if x_parent and y_parent:
                return False
        return False
        