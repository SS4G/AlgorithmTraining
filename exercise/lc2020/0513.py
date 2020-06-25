class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def findBottomLeftValue(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        currentMaxDepth = [-1, ]
        currentLeftValue = [None, ]

        self.dfsHelper(root, 0, currentMaxDepth, currentLeftValue)
        return currentLeftValue[0]
    
    def dfsHelper(self, root, currentDepth, currentMaxDepth, currentLeftValue):
        if root is None:
            return
        if currentDepth > currentMaxDepth[0]:
            currentMaxDepth[0] = currentDepth
            currentLeftValue[0] = root.val

        self.dfsHelper(root.left, currentDepth + 1, currentMaxDepth, currentLeftValue)
        self.dfsHelper(root.right, currentDepth + 1, currentMaxDepth, currentLeftValue)

