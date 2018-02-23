from AlgorithmTraining.G55Utils.Py.Utils import *
class Solution:
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        kcnt = [0, ]
        ksmallest = [0, ]
        self.traverseRecure(root, kcnt, ksmallest, k)
        return ksmallest[0]

    def traverseRecure(self, root, kcnt, ksmallest, k):
        if root is not None:
            self.traverseRecure(root.left, kcnt, ksmallest, k)
            kcnt[0] += 1
            if kcnt[0] == k:
                ksmallest[0] = root.val
            self.traverseRecure(root.right, kcnt, ksmallest, k)

