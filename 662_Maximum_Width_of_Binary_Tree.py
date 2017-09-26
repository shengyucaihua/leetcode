# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def widthOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        q=[(root,1)]
        ans=0
        while q:
            width=q[-1][-1]-q[0][-1]+1
            ans=max(ans,width)
            q_new=[]
            for node, value in q:
                if node.left:
                    q_new.append((node.left,2*value))
                if node.right:
                    q_new.append((node.right,2*value+1))
            q=q_new
        return ans