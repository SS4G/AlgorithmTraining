from AlgorithmTraining.G55Utils.Py.Utils import *
class Solution(object):
    def convertBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        sum = []
        self.traverse(root, sum)
        return sum[0]

    def traverse(self, root, sum):
        if root is not None:
            rightSum = self.traverse(root.right, sum)
            sum[0] += root.val
            root.val = sum[0]
            leftSum = self.traverse(root.left, sum)