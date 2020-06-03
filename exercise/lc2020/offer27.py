class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def mirrorTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if root is None:
            return None
        left_mirror = self.mirrorTree(root.left)
        right_mirror = self.mirrorTree(root.right) 
        resRoot = TreeNode(root.val)
        resRoot.left = right_mirror 
        resRoot.right = left_mirror
        return resRoot

