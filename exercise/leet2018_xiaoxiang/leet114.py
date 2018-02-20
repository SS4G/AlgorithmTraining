from AlgorithmTraining.G55Utils.Py.Utils import *

class Solution:
    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        self.flattenRecure(root)

    def flattenRecure(self, root):
        """
        :param root:
        :return: bottom of the sub tree
        """
        if root is None:
            return None
        elif root.left is None and root.right is None:
            return root
        else:
            rightRoot = root.right
            rightBottom = self.flattenRecure(root.right)
            leftRoot = root.left
            leftBottom = self.flattenRecure(root.left)
            wholeBottom = root
            if leftBottom is not None:
                wholeBottom.right = leftRoot
                wholeBottom.left = None
                wholeBottom = leftBottom
            if rightBottom is not None:
                wholeBottom.right = rightRoot
                wholeBottom.left = None
                wholeBottom = rightBottom
            return wholeBottom

if __name__ == "__main__":
    s = Solution()
    root = TreeUtil.deserialize([1, 2, 5, 3, 4, None, 6])
    TreeUtil.showTree(root)
    s.flatten(root)
    TreeUtil.showTree(root)