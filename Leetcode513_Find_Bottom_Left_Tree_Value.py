# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def findBottomLeftValue(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        qa=[root]
        while qa:
            qb=[]
            for n in qa:
                if n.left:
                    qb.append(n.left)
                if n.right:
                    qb.append(n.right)
            if not qb:
                return qa[0].val
            qa=qb
        return None